import streamlit as st
from PIL import Image
import base64
import io

def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def show():

    st.markdown("""
    <h1 style='text-align: center;'>
        Breaking The  <span style='color: #ff9900;'>Linear Assumption</span>
    </h1>
""", unsafe_allow_html=True)
    

    image1 = Image.open("images/john.jpg").resize((400, 400))
    image2 = Image.open("images/robert.png").resize((400, 400))

    st.markdown("""
    <style>
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 50px;
    }
    .image-wrapper {
        text-align: center;
    }
    .image-caption {
        margin-top: 10px;
        color: #1c0030;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="image-container">
        <div class="image-wrapper">
            <img src="data:image/png;base64,{}" width="300">
            <p class="image-caption">John Nelder</p>
        </div>
        <div class="image-wrapper">
            <img src="data:image/png;base64,{}" width="300">
            <p class="image-caption">Robert Wedderburn</p>
        </div>
    </div>
    """.format(image_to_base64(image1), image_to_base64(image2)), unsafe_allow_html=True)


    st.write("""
    Generalized Linear Models (GLMs) emerged as a powerful extension of traditional statistical methods to address the limitations of Multiple Linear Regression. This development can be traced back to the early 20th century, when statisticians recognized the need for a more flexible modeling framework that could accommodate various types of data. A landmark event in this progression occurred in 1972, when John Nelder and Robert Wedderburn published a seminal paper introducing GLMs. Their work unified various statistical models, such as linear regression, logistic regression, and Poisson regression, under a single theoretical framework. The inception of GLMs was largely motivated by several critical questions:

    *What if the response variable does not follow a normal distribution, such as when it adheres to a Binomial or Poisson distribution?*
    Moreover, in the realm of Multiple Linear Regression, it is assumed that residuals maintain constant variance - a condition known as homoscedasticity. 
             
    However, *what if the residuals exhibit non-constant variance, a phenomenon frequently encountered in real-world data?*
    Furthermore, Multiple Linear Regression presupposes a linear relationship between the predictors and the response variable. Yet, *what if the actual relationships are non-linear, thus complicating the modeling process?*
             
    Lastly, the traditional framework of Multiple Linear Regression is predominantly suited for continuous response variables. This raises the important question of how well this approach can perform when applied to count or categorical data types. By addressing these critical inquiries, GLMs provide a robust and versatile framework that extends the applicability of regression analysis to a broader range of statistical challenges.

    """)

    st.subheader("The Vital Pieces of GLMs")

    st.write("""
    **Random Component**: The random component of a GLM represents the distribution of the response variable, which can differ from the normal distribution assumed in standard linear regression. Some common distributions used in GLMs include:

    - **Binomial Distribution**: Used for binary outcome data, such as success/failure or yes/no responses. Example datasets include medical trial outcomes (e.g., whether a patient improves after treatment) or survey responses (e.g., whether a respondent prefers one product over another).
    - **Poisson Distribution**: Suitable for count data, where the response variable represents the number of occurrences of an event in a fixed interval. Examples include the number of accidents at an intersection per year or the number of customer arrivals at a store within an hour.
    - **Gamma Distribution**: Used for continuous, positively skewed data, such as time until an event occurs or insurance claims. An example dataset might include the duration of hospital stays.
    - **Inverse Gaussian Distribution**: Often applied in survival analysis and modeling time-to-event data. An example could be the time until a patient experiences a specific medical event.
    - **Normal Distribution**: Although GLMs can include normal errors, they are primarily used when the response variable is continuous and normally distributed.

    **Systematic Component**: The systematic component of a GLM is represented as $$ g(y) = x \\beta $$, where:
    - $$ g(p) $$ is the linear predictor that transforms the response variable.
    - $$ x $$ is the vector of predictor variables (independent variables).
    - $$ \\beta $$ is the vector of coefficients associated with the predictors.
   
    This component models the relationship between the predictors and the response variable through a linear combination of the predictors.

    **Link Function**: The link function connects the random component to the systematic component by transforming the expected value of the response variable $$ E(y) $$ to the linear predictor. Common link functions include:
    $$ g(p) = \\log\\left( \\frac{p}{1-p} \\right) $$

    - **Logit Link Function**: Used in logistic regression for binary response variables. It links the probability of success to the linear predictor: $$ g(p) = \\log\\left( \\frac{p}{1-p} \\right) $$
    - **Probit Link Function**: Also used for binary outcomes but assumes a normal distribution of the latent variable. It transforms probabilities into standard normal deviations.
    - **Log Link Function**: Commonly used for count data in Poisson regression, where it links the expected count to the linear predictor: $$ g(\\lambda) = \\log(\\lambda) $$
    - **Identity Link Function**: Used when the response variable is continuous and normally distributed, making it equivalent to ordinary least squares regression.
    - **Inverse Link Function**: Often applied in gamma regression, it models a response variable that is positive and continuous: $$ g(y) = \\frac{1}{y} $$
    
    After understanding the fundamental components of GLMs, we can now explore how these elements come together to model different types of distributions, adapting to the specific characteristics of the data at hand.
    """)

    st.markdown("""
    <div style='background-color: #fab246; padding: 10px; border-radius: 5px;'>
        <span style='color: #1c0030; font-size: 20px; font-family: "Courier Prime", monospace;'>
            <em>In our exploration here, we’ll shine a light on the core trio of statistical modeling - the Binomial, Poisson, and Gamma distributions - leveraging GLMs to understand their role in data science.</em>
        </span>
    </div>
    """, 
    unsafe_allow_html=True)
