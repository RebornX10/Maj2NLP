import pandas as pd
import re
import difflib

# Read in the two CSV files using pandas
questions_df = pd.read_csv('questions.csv')
answers_df = pd.read_csv('answers.csv')

# Function to find the most similar question in the questions CSV
def find_similar_question(question):
    # Initialize a variable to store the highest similarity score
    highest_similarity = 0
    # Initialize a variable to store the most similar question
    most_similar_question = ''
    
    # Iterate through each question in the questions CSV
    for index, row in questions_df.iterrows():
        # Get the question text
        q = row['question']
        # Calculate the similarity score using difflib
        similarity = difflib.SequenceMatcher(None, question, q).ratio()
        # If the similarity score is higher than the current highest, update the highest and most similar question
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_question = q
    
    # Return the most similar question
    return most_similar_question

# Function to find the most relevant answer
def find_relevant_answer(question):
    # Find the most similar question using the function above
    most_similar_question = find_similar_question(question)
    # Get the ID of the most similar question
    question_id = questions_df[questions_df['question'] == most_similar_question]['ID'].values[0]
    # Get the answers for the most similar question
    answers = answers_df[answers_df['ParentID'] == question_id]
    # Sort the answers by relevancy score
    answers = answers.sort_values(by=['answer_relevancy_score'], ascending=False)
    # Return the most relevant answer
    return answers['answer'].values[0]

# Test the smartFAQ with a sample question
question = 'What is the capital of France?'
answer = find_relevant_answer(question)
print(answer)  # Output: "Paris"
