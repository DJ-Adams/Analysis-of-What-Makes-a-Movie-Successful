import streamlit as st
import json
# Create multiple pages from apps in pages folder
st.set_page_config()
FILEPATHS_FILE = 'config/filepaths.json'
with open(FILEPATHS_FILE) as f:
    FPATHS = json.load(f)
st.write('# Movie Reviews and Ratings Predictor')
st.write('##  Exploratory Analysis Visuals')

st.subheader('Frequency Distribution of Words from Positive Reviews ')

st.image('eda/hfreq.png')

st.subheader('Frequency Distribution of Words from Negative Reviews ')

st.image('eda/lfreq.png')

st.subheader('Trigrams from High Reviews ')

st.image('eda/trihigh.png')

st.subheader('Trigrams from Low Reviews ')

st.image('eda/trilow.png')

st.subheader('Word Clouds ')

st.image('eda/word_cloud.png')