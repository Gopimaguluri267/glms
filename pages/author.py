import streamlit as st
import base64

def show():
    st.markdown("""
        <h1 style='text-align: center;'>
            <span style='color: #ff9900;'>Contributors</span>
        </h1>
    """, unsafe_allow_html=True)

    people = [
        {"name": "Gopi Maguluri", "linkedin": "https://www.linkedin.com/in/gopimaguluri2267"},
        {"name": "Pooja Baralu Umesh", "linkedin": "https://www.linkedin.com/in/pooja-baraluumesh"},
        {"name": "Satya Lasya Narendrapurapu", "linkedin": "https://www.linkedin.com/in/satya-lasya-n-0169a081"},
        {"name": "Venkatachalam Subramanian Periya Subbu", "linkedin": "https://www.linkedin.com/in/venkatachalam-subramanian-periya-subbu"}
    ]

    linkedin_icon_path = 'images/linkedin_icon.png'

    with open(linkedin_icon_path, "rb") as image_file:
        linkedin_icon_base64 = base64.b64encode(image_file.read()).decode()

    st.markdown("""
    <style>
    .name-button {
        display: inline-block;
        padding: 5px 10px;
        background-color: transparent;
        color: #1c0030;
        text-decoration: none;
        font-size: 18px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .name-button:hover {
        background-color: #fac069;
    }
    .linkedin-icon {
        height: 16px;
        width: 16px;
        margin-left: 5px;
        vertical-align: middle;
    }
    </style>
    """, unsafe_allow_html=True)

    names_html = ""
    for person in people:
        names_html += f"""
        <a href="{person['linkedin']}" target="_blank" class="name-button">
            {person['name']}
            <img src="data:image/png;base64,{linkedin_icon_base64}" class="linkedin-icon">
        </a>
        <br><br>
        """

    st.markdown(names_html, unsafe_allow_html=True)

    st.markdown("""
            <div style='position: fixed; bottom: 20px; left: 60%; transform: translateX(-40%);'>
                <h3 style='font-size: 18px; color: #1c0030; font-family: "Courier New", Courier, monospace;'>
                    Made with ❤️ - USF-MSDS-601
                </h3>
            </div>
            """, unsafe_allow_html=True)
