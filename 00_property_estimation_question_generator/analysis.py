import pandas as pd

# Read the generated questions from a Parquet file
parquet_file = 'generated_questions.parquet'

# Save the DataFrame to a Parquet file
df_read = pd.read_parquet(parquet_file, engine='pyarrow')

print("Rows in the DataFrame:", len(df_read))