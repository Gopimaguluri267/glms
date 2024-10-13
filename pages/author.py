import streamlit as st
import base64

def show():
    st.markdown("<h1 style='text-align: center; color: #ff9900;'>Contributors</h1>", unsafe_allow_html=True)

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
    .contributor {
        font-size: 18px;
        color: #1c0030;
        margin-bottom: 10px;
    }
    .guide {
        font-size: 20px;
        font-weight: bold;
        color: #1c0030;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .linkedin-icon {
        height: 16px;
        width: 16px;
        margin-left: 5px;
        vertical-align: middle;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guide">
        Guided by: 
        <a href="https://www.linkedin.com/in/cody-j-carroll/" target="_blank">
            Cody Carroll
            <img src="data:image/png;base64,{linkedin_icon_base64}" class="linkedin-icon">
        </a>
    </div>
    """, unsafe_allow_html=True)

    for person in people:
        st.markdown(f"""
        <div class="contributor">
            <a href="{person['linkedin']}" target="_blank">
                {person['name']}
                <img src="data:image/png;base64,{linkedin_icon_base64}" class="linkedin-icon">
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style='position: fixed; bottom: 20px; left: 57%; transform: translateX(-43%);'>
        <h3 style='font-size: 18px; color: #1c0030; font-family: "Courier New", Courier, monospace;'>
            Made with ❤️ - USF-MSDS-601-Fall24
        </h3>
    </div>
    """, unsafe_allow_html=True)
