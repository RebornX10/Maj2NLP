import sys

import pandas as pd
import re
import difflib

questions_df = pd.read_csv('data/questions_preprocessed.csv', encoding_errors='replace')
answers_df = pd.read_csv('data/answers_preprocessed.csv', encoding_errors='replace')


def find_similar_question(question):
    highest_similarity = 0
    most_similar_question = ''

    for index, row in questions_df.iterrows():
        q = row['Title']
        #q = [str(x) for x in q]
        # [print(x) for x in q if not isinstance(x, str)]
        similarity = difflib.SequenceMatcher(None, question, q).ratio()
        #print(similarity)
        # If the similarity score is higher than the current highest, update the highest and most similar question
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_question = q

    # Return the most similar question
    return most_similar_question


# Function to find the most relevant answer
def find_relevant_answer(question):
    most_similar_question = find_similar_question(question)
    question_id = questions_df[questions_df['Body'] == most_similar_question]['Id'].values
    answers = answers_df[answers_df['ParentId'] == question_id]
    answers = answers.sort_values(by=['Score'], ascending=False)
    return answers['Body'].values


def chatter(question):
    if question.lower() == 'exit':
        print('Exiting chatbot...')
        sys.exit()
    # Find and display the relevant answer
    answer = find_relevant_answer(question)
    print(answer)

chatter("download a file over http")