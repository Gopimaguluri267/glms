import streamlit as st
from PIL import Image
import base64
import io

def show():

    st.markdown("""
        <h1 style='text-align: center;'>
            The <span style='color: #ff9900;'>Knowledge Bank</span> We Are <span style='color: #ff9900;'>Grateful</span> For
        </h1>
    """, unsafe_allow_html=True)

    st.write("""
    - [Generalized Linear Models - Wikipedia](https://en.wikipedia.org/wiki/Generalized_linear_model)
    - [A Quick History of GLMs - Revolution Analytics](https://blog.revolutionanalytics.com/2014/05/quick-history-glm.html)
    - [Introduction to Generalized Linear Models - Medium](https://medium.com/@sahin.samia/a-comprehensive-introduction-to-generalized-linear-models-fd773d460c1d)
    - [Generalized Linear Models - Encyclopedia of Math](https://encyclopediaofmath.org/wiki/Generalized_linear_models)
    - [Poisson Regression for Count Data - Medium](https://medium.com/data-analytics-magazine/master-poisson-regression-the-ultimate-machine-learning-hack-for-count-data-25b5f439ddc5)
    - [Poisson vs Linear Regression - Daily Dose of Data Science](https://blog.dailydoseofds.com/p/poisson-regression-vs-linear-regression)
    - [Poisson Regression Chapter - Beyond Multiple Linear Regression](https://bookdown.org/roback/bookdown-BeyondMLR/ch-poissonreg.html)
    - [Understanding Logistic Regression - Geeks for Geeks](https://www.geeksforgeeks.org/understanding-logistic-regression/)
    - [Logistic Regression Simplified - Medium](https://medium.com/data-science-group-iitr/logistic-regression-simplified-9b4efe801389)
    - [Logistic Regression Blog - V7 Labs](https://www.v7labs.com/blog/logistic-regression)
    - [Logistic Regression for Beginners - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2021/08/conceptual-understanding-of-logistic-regression-for-data-science-beginners/)
    - [Logistic Regression Video - YouTube](https://youtu.be/SqN-qlQOM5A?si=_XieZZv5zf-aIkbj)
    - [GLM and Poisson Regression - YouTube](https://bit.ly/2ZMSv4U)
    - [Poisson Regression Explained - YouTube](https://www.youtube.com/watch?v=HmMag6EvNyQ)
    - [Getting Started with Gamma Regression - UVA Library](https://library.virginia.edu/data/articles/getting-started-with-gamma-regression)
    - [Gamma Regression - Penn State Online](https://online.stat.psu.edu/stat462/node/211/)
    - [Gamma Regression Video - YouTube](https://youtu.be/DDP62EUMRFs?si=F0I_GCEOJRYD9N4M)
    - [GLM Tutorial Series - YouTube](https://www.youtube.com/playlist?list=PLJ71tqAZr197DkSiGT7DD9dMYxkyZX0ti)
    """)


    st.markdown("""
            <div style='position: fixed; bottom: 20px; left: 60%; transform: translateX(-40%);'>
                <h3 style='font-size: 18px; color: #1c0030; font-family: "Courier New", Courier, monospace;'>
                    Made with ❤️ - USF-MSDS-601
                </h3>
            </div>
            """, unsafe_allow_html=True)
