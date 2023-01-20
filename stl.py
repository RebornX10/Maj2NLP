import streamlit as st
import pandas as pd
from chatbot import chatter

st.title('Chatbot')


@st.cache
def load_data(data_location):
    data = pd.read_csv(data_location, encoding_errors='replace')
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


data_load_state = st.text("Loading Data")
answers = load_data("data/answers_preprocessed.csv")
questions = load_data("data/questions_preprocessed.csv")
data_load_state.text("Data Loaded")

if st.checkbox(f'Show raw data'):
    st.subheader('Raw data')
    st.write(questions)
    st.write(answers)

prompt = st.text_area("Ask any question", max_chars=120, placeholder="How to download a file over http Python",
                      label_visibility="visible")

st.write('Most relevant answer:', str(chatter(prompt)))
