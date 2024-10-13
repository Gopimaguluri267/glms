import streamlit as st

def show():
    st.markdown("""
    <h1 style='text-align: center;'>
        <span style='color: #ff9900;'>The Takeaway</span>
    </h1>
""", unsafe_allow_html=True)
    
    st.write("""
    In essence, GLMs elegantly navigate the complexities of diverse data, paving the way for more accurate modeling.
    
             
    Overall, Generalized Linear Models provide a powerful framework for modeling data that don’t align with the assumptions made for standard linear regression models, particularly when dealing with non-normal, skewed, well bounded, count or continuous with limited domain distributions like the Binomial, Poisson, Gamma distribution discussed throughout the article. By linking the expected value of the target variable to a linear predictor through an appropriate link function, GLMs offer the flexibility to capture complex relationships and information in data, such as those involving varying variance or diminishing returns.
             

    If you are an aspiring Data Scientist, Statistician, Actuary, Economist or an Epidemiologist, you will definitely need the Generalized Linear Models. As a data scientist or statistician, you would use GLMs to model non-normal data, make predictions, and understand relationships between variables that do not fit the assumptions of traditional linear models. For instance, you might use GLMs to model customer spending behavior, product demand, or risk factors. As an actuary, you would use GLM in risk assessment and pricing particularly to model claims data, which are typically non-normal and have high variability. As an epidemiologist, you would find yourself using GLMs to study factors affecting disease spread and healthcare outcomes, like how healthcare professionals did during the covid pandemic.
    
             
    In a world where data is far from "normal", GLMs offer a robust and reliable way to extract meaningful insights, transforming complexity into actionable models. 
    """)

    st.markdown("""
    <div style='background-color: #fab246; padding: 10px; border-radius: 5px;'>
        <span style='color: #1c0030; font-size: 20px; font-family: "Courier Prime", monospace;'>
            <em>Let’s turn data chaos into linear order, one link function at a time.</em>
        </span>
    </div>
    """, unsafe_allow_html=True)
