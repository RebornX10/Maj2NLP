import sys

import pandas as pd
import re
import difflib
from preprocess import clean_quest
from cdifflib import CSequenceMatcher
import time
difflib.SequenceMatcher = CSequenceMatcher

questions_df = pd.read_csv('data/questions_preprocessed.csv', encoding_errors='replace')
answers_df = pd.read_csv('data/answers_preprocessed.csv', encoding_errors='replace')


def time_execution(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print("Execution time: ", end_time - start_time)
        return result
    return wrapper

def find_similar_question(question):
    highest_similarity = 0
    most_similar_question = ''

    for index, row in questions_df.iterrows():
        q = str(row['Title'])
        similarity = difflib.SequenceMatcher(None, question, q).ratio()
        #print(similarity)
        # If the similarity score is higher than the current highest, update the highest and most similar question
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_question = q
    # Return the most similar question
    print(most_similar_question)
    return most_similar_question


# Function to find the most relevant answer
def find_relevant_answer(question):
    most_similar_question = find_similar_question(question)
    question_id = questions_df[questions_df['Title'] == most_similar_question]['Id'].values
    print(question_id)
    answers = answers_df[answers_df['ParentId'] == question_id[0]]
    answers = answers.sort_values(by=['Score'], ascending=False)
    return answers['Body'].values

@time_execution
def chatter(question):
    question = clean_quest(question)
    if question.lower() == 'exit':
        print('Exiting chatbot...')
        sys.exit()
    # Find and display the relevant answer
    answer = find_relevant_answer(question)
    print(answer)
    return answer[0]

chatter("download file over http")