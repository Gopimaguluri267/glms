import streamlit as st
from pages import introduction, title, linear_regression, logistic_regression,\
    gamma_regression, poisson_regression, conclusion, references, author

st.set_page_config(page_title="Generalized Linear Models", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Courier+Prime&display=swap');
    
    .stApp {
        background-color: #f0e6ff;
    }
    .stSidebar {
        background-color: #d9c3ff;
    }
    .stButton>button {
        background-color: #8a2be2;
        color: white;
    }
    .stButton>button:hover {
        background-color: #9b30ff;
    }
    h1, h2, h3 {
        color: #4b0082;
    }
    p, li {
        color: #1c0030;
        font-family: 'Courier Prime', monospace;
        font-size: 20px;
    }
    .tile {
        background-color: #8a2be2;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        cursor: pointer;
        text-align: center;
        transition: background-color 0.3s;
    }
    .tile:hover {
        background-color: #9b30ff;
    }
    .selected {
        background-color: #4b0082;
    }
    [data-testid="stSidebarNav"], header, .css-1v0mbdj, .css-1d391kg {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Chapters")

pages = {
    "Title": title,
    "Introduction": introduction,
    "Linear Regression": linear_regression,
    "Logistic Regression": logistic_regression,
    "Poisson Regression": poisson_regression,
    "Gamma Regression": gamma_regression,
    "Conclusion": conclusion,
    "References": references,
    "Authors": author
}

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Title"

for page_name in pages:
    if st.sidebar.button(page_name, key=page_name):
        st.session_state.current_page = page_name

current_page_module = pages[st.session_state.current_page]
current_page_module.show()
