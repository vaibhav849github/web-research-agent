import streamlit as st
from main import run_agent

st.title('Web Research Agent')

user_query = st.text_input('Enter your research query:', '')

if user_query:
    st.write('Running agent...')
    result = run_agent(user_query)
    st.write('=== Research Summary ===')
    st.write(result)
else:
    st.write('Please enter a research query above.')