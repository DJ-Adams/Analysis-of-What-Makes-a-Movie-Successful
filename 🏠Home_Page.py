import streamlit as st
import json
# Create multiple pages from apps in pages folder
st.set_page_config()
FILEPATHS_FILE = 'config/filepaths.json'
with open(FILEPATHS_FILE) as f:
    FPATHS = json.load(f)
st.write('# Movie Reviews and Ratings Predictor')
st.image('Images/Movie_Bill.jpg')
st.sidebar.success('Select a page above')
st.markdown(
    '''**👈🏾 Select a page from the sidebar**'''
)


import streamlit.components.v1 as components 
# Source: https://meta.stackoverflow.com/questions/392785/need-to-add-linkedin-and-github-badges-in-profile-page-of-stack-overflow
links_html = """<ul>
<li><a href="https://github.com/DJ-Adams/Analysis-of-What-Makes-a-Movie-Successful">Project Repo</a></li>
  <li><a href="www.linkedin.com/in/darlene-adams-90939811a/[removed]" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
  </a> </li>
  <li><a href="https://github.com/DJ-Adams" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
  </a></li>
</ul>"""
components.html(links_html)


# Open and display a .md file
with open("Analysis_Overview.md") as f:
    readme = f.read()
st.markdown(Analysis_Overview)