import streamlit as st
import numpy as np
from pages.linear_model_template import show_model_page

def show():
    
    st.markdown("""
    <h1 style='text-align: center;'>
        <span style='text-decoration: line-through; color: #ff9900;'>Extra</span>
        "Ordinary" Tool
    </h1>
""", unsafe_allow_html=True)

    st.write(""" Ordinary Linear Regression, the first weapon used to model any variable. It is a process of fitting a line to a set of data points with the intent of reducing the sum of squared errors (Method of OLS) or maximizing the likelihood of observing the observed data (Method of MLE). 

    Basically It aims to establish a linear relationship between one or more independent variables (predictors) and a dependent variable (outcome). Its primary goal is to find the best-fitting straight line through a set of data points, allowing us to understand and predict the behavior of the dependent variable based on the independent variables.""")

    st.write("### (i) Fundamentals")
    st.write("""
    As discussed earlier, linear regression models the relationship between a dependent variable Y and one or more independent variables X by fitting a linear equation to the observed data. The simplest form is:
    """)
    st.latex(r"Y = \beta_0 + \beta_1X + \epsilon")
    st.write("""
    Where:
    - Y is the dependent variable we're trying to predict
    - X is the independent variable (predictor)
    - β₀ is the y-intercept (the value of Y when X = 0)
    - β₁ is the slope (the change in Y for a one-unit increase in X)
    - ε is the error term (the part of Y the model doesn't explain)
    """)

    st.write("### 2. Assumptions")
    st.write("""
    Ordinary Linear Regression relies on several key assumptions:
    1. Linearity: The relationship between X and Y is linear
    2. Independence: Observations are independent of each other
    3. Homoscedasticity: The variance of the residuals is constant
    4. Normality: The residuals are normally distributed
    5. No multicollinearity: Independent variables are not highly correlated with each other
    """)

    st.write("### 3. Estimation Method")
    st.write("""
    The most common method for estimating the parameters (β₀ and β₁) is Ordinary Least Squares (OLS). OLS minimizes the sum of the squared residuals:
    """)
    st.latex(r"\text{minimize} \sum_{i=1}^n (y_i - (\beta_0 + \beta_1x_i))^2")

    st.write("### 4. Multiple Linear Regression")
    st.write("""
    When we have multiple predictors, the model extends to:
    """)
    st.latex(r"Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_pX_p + \epsilon")

    st.write("### 5. Model Evaluation")
    st.write("""
    We have a bag of multiple metrics to evaluate the performance of the model, some of them are: 
    1. R-squared (R²): Proportion of variance in outcome variable explained by the set predictor variables
    2. Adjusted R-squared: R² adjusted for the number of predictors
    3. F-statistic: Tests the overall significance of the model
    4. t-statistics: Test the significance of individual predictors
    5. Residual plots: Visual checks for assumption violations
    """)

    st.write("""
        While powerful and amazing, Ordinary Linear Regression has limitations:
    1. It assumes a linear relationship, which may not always hold (exactly what we address here !)
    2. It's sensitive to outliers
    3. It assumes the residuals are normally distributed and have constant variance

        These limitations lead to various extensions and alternatives. One among them being Generalized Linear Models. 
        """)

    st.markdown("""
        <div>
            <span style='color: #ff9900; font-size: 20px; font-family: "Courier Prime", monospace;'>
                <em>Check out the following chapters to learn more and definitely expand your arsenal for modeling</em>
            </span>
        </div>
        """, unsafe_allow_html=True)

    show_model_page(
        "Linear Regression",
    )
