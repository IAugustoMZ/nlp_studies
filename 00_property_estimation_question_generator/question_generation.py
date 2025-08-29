import os
import numpy as np
import pandas as pd
from dimensions import QuestionsDimensions

def generate_questions(dimensions: QuestionsDimensions, n):
    """
    Generate a list of questions based on the provided dimensions.

    Args:
        dimensions (QuestionsDimensions): The dimensions to base the questions on.
        n (int): The number of questions to generate.

    Returns:
        list: A list of generated questions.
    """
    questions = []
    question_marks = ["What is the", 'Give me the', 'Can you tell me the', 'Please provide the', 'Provide me with the', 'Table the', 'List the', 'Show me the', 'What are the', 'Graph the', 'Plot the', 'Give a table of the', 'Give a graph of the', 'Give a plot of the', 'Show a table of the', 'Show a graph of the', 'Show a plot of the', 'Provide a table of the', 'Provide a graph of the', 'Provide a plot of the']

    template_query_only = '{mark} {property} of {compound}'
    template_correlation = '{mark} {state} {property} of {compound} {temperature_format} {temperature_input} {temperature_input_unit}'

    for i in range(n):
        # randomly select a chemical compound, a physical state, and a property
        compound = np.random.choice([c[0] for c in dimensions.chemical_compounds])
        state = np.random.choice([c[0] for c in dimensions.physical_states])
        property_ = dimensions.physical_properties[np.random.randint(len(dimensions.physical_properties))]
        output_unit = property_[1]
        property_name = property_[2]
        isquery_only = property_[3]

        # get a synonym for the property
        property_synonym = np.random.choice(dimensions.physical_property_synonyms[property_[0]])

        # randomly select a question mark
        if isquery_only:
            filtered_marks = [mark for mark in question_marks if all(x not in mark.lower() for x in ['table', 'plot', 'graph'])]
            question_mark = np.random.choice(filtered_marks)
        else:
            question_mark = np.random.choice(question_marks)


        # Sample from a Bernoulli distribution with p=0.5
        ask_output_unit = np.random.binomial(1, 0.5)

        if isquery_only:
            if ask_output_unit and output_unit != '-':
                output_unit = np.random.choice(dimensions.output_units[output_unit])

                question = template_query_only.format(
                    mark=question_mark,
                    property=property_synonym,
                    compound=compound
                ) + f' in {output_unit}'
            else:
                question = template_query_only.format(
                    mark=question_mark,
                    property=property_synonym,
                    compound=compound
                )
            state = 'None'
            temperature_input = 'None'
            temperature_input_unit = 'None'
            pressure_input = 'None'
            pressure_input_unit = 'None'
        else:
            # check if plot, graph or table is in the question mark
            if any(x in question_mark.lower() for x in ['table', 'plot', 'graph']):
                # if it is, we need to add the temperature input
                t1 = round(np.random.uniform(0, 1000), 2)  # random temperature input
                t2 = round(np.random.uniform(0, 1000), 2)  # random temperature input
                min_temp = min(t1, t2)
                max_temp = max(t1, t2)
                if min_temp == max_temp:
                    temperature_format = np.random.choice(['at T', 'at temperature', 'in temperature', 'in T', 'at temp', 'in temp'])
                    temperature_input = f'{min_temp:.2f}'
                else:
                    temperature_format = 'between'
                    temperature_input = f'{min_temp:.2f} and {max_temp:.2f}'
            else:
                temperature_format = np.random.choice(['at T', 'at temperature', 'in temperature', 'in T', 'at temp', 'in temp'])
                temperature_input = round(np.random.uniform(0, 1000), 2)
            temperature_input_unit = np.random.choice(dimensions.temperature_units)

            # consider the case where the state is None
            if property_[0] in ['vapor_pressure', 'enthalpy_vaporization']:
                state = ''

            if ask_output_unit and output_unit != '-':
                output_unit = np.random.choice(dimensions.output_units[output_unit])

                question = template_correlation.format(
                    mark=question_mark,
                    state=state,
                    property=property_synonym,
                    compound=compound,
                    temperature_format=temperature_format,
                    temperature_input=temperature_input,
                    temperature_input_unit=temperature_input_unit
                ) + f' in {output_unit}'
            else:
                question = template_correlation.format(
                    mark=question_mark,
                    state=state,
                    property=property_synonym,
                    compound=compound,
                    temperature_format=temperature_format,
                    temperature_input=temperature_input,
                    temperature_input_unit=temperature_input_unit
                )

            if property_[0] == 'density' and state == 'vapor':
                pressure_format = np.random.choice(['at P', 'at pressure', 'in pressure', 'in P'])
                pressure_input = round(np.random.uniform(0, 1000), 2)
                pressure_input_unit = np.random.choice(dimensions.pressure_units)
                question += f' {pressure_format} {pressure_input:.2f} {pressure_input_unit}'
            else:
                # Sample from a Bernoulli distribution with p=0.5
                ask_diff_pressure = np.random.binomial(1, 0.5)
                if ask_diff_pressure:
                    pressure_format = np.random.choice(['at P', 'at pressure', 'in pressure', 'in P'])
                    pressure_input = round(np.random.uniform(0, 1000), 2)
                    pressure_input_unit = np.random.choice(dimensions.pressure_units)
                    question += f' {pressure_format} {pressure_input:.2f} {pressure_input_unit}'
                else:
                    pressure_input = 'None'
                    pressure_input_unit = 'None'

        if state == '':
            state = 'None'

        # format object
        questions.append(
            {
                'question': str(question),
                'compound': str(compound),
                'property': str(property_[0]),
                'state': str(state),
                'output_unit': str(output_unit),
                'temperature_input': str(temperature_input),
                'pressure_input': str(pressure_input),
                'temperature_input_unit': str(temperature_input_unit),
                'pressure_input_unit': str(pressure_input_unit),
            }
        )
    
    return questions


if __name__ == "__main__":
    n = int(input("Enter the number of questions to generate: "))
    set_ = input("Enter the set to be generated: ").strip().lower()
    dimensions = QuestionsDimensions()

    questions = generate_questions(dimensions, n)
    for question in questions:
        print("Generated Question:")
        print(question)
        print('-' * 40)

    df = pd.DataFrame(questions)
    parquet_file = f"generated_questions_{set_}.parquet"
    try:
        import pyarrow  # noqa: F401
        parquet_engine = "pyarrow"
    except ImportError:
        try:
            import fastparquet  # noqa: F401
            parquet_engine = "fastparquet"
        except ImportError:
            raise ImportError(
                "Neither 'pyarrow' nor 'fastparquet' is installed. "
                "Please install one of them for parquet support."
            )

    if os.path.exists(parquet_file):
        existing_df = pd.read_parquet(parquet_file, engine=parquet_engine)
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        combined_df.to_parquet(parquet_file, index=False, engine=parquet_engine)
    else:
        df.to_parquet(parquet_file, index=False, engine=parquet_engine)
    print("Questions saved to generated_questions.parquet")

    df_read = pd.read_parquet(parquet_file, engine=parquet_engine)
    print(f"Total number of questions in {parquet_file}: {len(df_read)}")
