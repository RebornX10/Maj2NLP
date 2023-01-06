import pandas as pd
import re
import difflib

# Read in the two CSV files using pandas
questions_df = pd.read_csv('data/questions_preprocessed.csv')
answers_df = pd.read_csv('data/answers_preprocessed.csv')

# Function to find the most similar question in the questions CSV
def find_similar_question(question):
    # Initialize a variable to store the highest similarity score
    highest_similarity = 0
    # Initialize a variable to store the most similar question
    most_similar_question = ''
    
    # Iterate through each question in the questions CSV
    for index, row in questions_df.iterrows():
        # Get the question text
        q = row['Title']
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
    question_id = questions_df[questions_df['Body'] == most_similar_question]['Id'].values[0]
    # Get the answers for the most similar question
    answers = answers_df[answers_df['ParentID'] == question_id]
    # Sort the answers by relevancy score
    answers = answers.sort_values(by=['Score'], ascending=False)
    # Return the most relevant answer
    return answers['Body'].values[0]

# Main loop of the chatbot
while True:
    # Get the user's question
    question = input('Please enter your question: ')
    # Check if the user wants to exit the chatbot
    if question.lower() == 'exit':
        print('Exiting chatbot...')
        break
    # Find and display the relevant answer
    answer = find_relevant_answer(question)
    print(answer)
