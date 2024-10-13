import streamlit as st
from PIL import Image
import base64
import io

def show():
    st.markdown("""
    <style>
    .title-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 70vh;
    }
    .title {
        text-align: center;
        color: #4b0082;
        font-family: "Courier New", Courier, monospace;
        margin: 0;
        padding: 0;
    }
    .subtitle {
        text-align: center;
        color: #ff9900;
        font-size: 36px;
        font-family: "Courier Prime", monospace;
        margin-top: 40px;
    }
    .footer {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
        font-size: 18px;
        color: #1c0030;
        font-family: "Courier New", Courier, monospace;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="title-container">
        <h1 class="title" style="font-size: 128px;">Generalized</h1>
        <h1 class="title" style="font-size: 120px;">Linear</h1>
        <h1 class="title" style="font-size: 92px;">Models</h1>
        <p class="subtitle">Because life isn't always "Normal"</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
            <div style='position: fixed; bottom: 20px; left: 60%; transform: translateX(-40%);'>
                <h3 style='font-size: 18px; color: #1c0030; font-family: "Courier New", Courier, monospace;'>
                    Made with ❤️ - USF-MSDS-601
                </h3>
            </div>
            """, unsafe_allow_html=True)
