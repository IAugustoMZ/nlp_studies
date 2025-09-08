# NLP Studies

This repository contains my studies and experiments in Natural Language Processing (NLP).

## Repository Structure

- **00_property_estimation_question_generator/**
	- Scripts for property estimation question generation, including:
		- `analysis.py`: Analysis tools and scripts.
		- `dimensions.py`: Dimension definitions and utilities.
		- `question_generation.py`: Logic for generating property estimation questions.

- **01_basic_nlp_course/**

		- Notebooks and materials for a basic NLP course, including:

			- `01_regular_expressions.ipynb`: Comprehensive introduction to regular expressions for NLP and chemical/process engineering. Includes:
				- Extraction of phone numbers, emails, chemical formulas, reaction equations, units, timestamps, error codes, simulation parameters, CAS numbers, and scientific notation.
				- Step-by-step pattern refinement and explanations.
				- Example-driven exercises with expected outputs and detailed markdown explanations.

			- `02_nltk_vs_spacy.ipynb`: Comparison of NLTK and spaCy for NLP tasks, including:
				- Tokenization, lemmatization, POS tagging, and named entity recognition.
				- Practical code examples and performance notes.

			- `03_language_processing_pipeline.ipynb`: Building and visualizing language processing pipelines in spaCy, with:
				- Custom pipeline components.
				- Practical examples and exercises.

			- `04_stemming_lemmatization.ipynb`: Introduction to stemming and lemmatization techniques in NLP, with:
				- Code examples for different algorithms.
				- Practical exercises and comparison of results.

			- `05_pos_tagging.ipynb`: Practical guide to Part-of-Speech (POS) tagging in NLP, including:
				- Examples and exercises using popular Python libraries.
				- Explanation of POS tag sets and their applications.

			- `06_named_entity_recognition.ipynb`: Introduction to Named Entity Recognition (NER):
				- Explanation of NER concepts and use cases.
				- Code examples using spaCy and NLTK.
				- Exercises for extracting and analyzing named entities.

			- `07_bag_of_words.ipynb`: Introduction to the Bag of Words model in NLP, including:
				- Theory and practical implementation.
				- Code examples for text vectorization.
				- Exercises and explanations for feature extraction and document-term matrices.

			- `08_stop_words_removal.ipynb`: Guide to stop words removal in NLP, including:
				- Theory and importance of stop words.
				- Code examples for removing stop words using different libraries.
				- Exercises and explanations for improving text preprocessing and feature extraction.
				
			- `09_bag_of_n_grams.ipynb`: Introduction to Bag of N-Grams in NLP, including:
				- Theory and practical implementation of n-gram models.
				- Code examples for extracting and using n-grams in text analysis.
				- Exercises and explanations for feature engineering with n-grams.
## Other Files

- `requirements.txt`: Python dependencies for the project.
- `Dockerfile` and `docker-compose.yml`: Docker configuration files for environment setup.
