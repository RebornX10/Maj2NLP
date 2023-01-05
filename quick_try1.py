import csv
import difflib

def get_most_similar_question(questions_csv, question):
  # Read in the questions CSV
  with open(questions_csv, 'r') as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    # Find the most similar question by comparing the Levenshtein distance
    # between the input question and each question in the CSV
    closest_question = difflib.get_close_matches(question, [row[1] for row in reader], n=1, cutoff=0.5)[0]
  return closest_question

def get_answer(answers_csv, closest_question):
  # Read in the answers CSV
  with open(answers_csv, 'r') as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    # Find the answer with the highest relevancy score for the closest question
    answer = sorted([row for row in reader if row[1] == closest_question], key=lambda x: x[2], reverse=True)[0]
  return answer

def main():
  # Read in the input question from the user
  question = input("Enter your question: ")
  # Get the most similar question from the questions CSV
  closest_question = get_most_similar_question('questions.csv', question)
  # Get the most relevant answer from the answers CSV
  answer = get_answer('answers.csv', closest_question)
  print(f"Here is the most relevant answer to your question: {answer[0]}")

if __name__ == '__main__':
  main()
