import tensorflow as tf
import tensorflow_text as text
import pandas as pd
# import train_test_split
from sklearn.model_selection import train_test_split

# Read in the two CSV files using pandas
questions = pd.read_csv('questions.csv')
answers = pd.read_csv('answers.csv')

# Preprocess the data
# ADD THE DATA

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(questions, answers, test_size=0.2)

# Create a TensorFlow dataset from the training data
train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))

# Create a TensorFlow dataset from the test data
test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test))

# Define the T5 model
t5 = text.T5(
    vocab_size=vocab_size,
    encoder_dim=128,
    decoder_dim=128,
    num_layers=2,
    max_seq_len=512
)

# Compile the model
t5.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
t5.fit(train_dataset, epochs=10)

# Evaluate the model on the test data
t5.evaluate(test_dataset)

# Main loop of the chatbot
while True:
    # Get the user's question
    question = input('Please enter your question: ')
    # Check if the user wants to exit the chatbot
    if question.lower() == 'exit':
        print('Exiting chatbot...')
        break
    # Preprocess the question
    # ADD THE DATA
    # Use the model to predict the most relevant answer
    answer = t5.predict(question)
    # Display the answer
    print(answer)
