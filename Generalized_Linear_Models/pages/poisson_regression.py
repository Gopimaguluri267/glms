import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from pages.poisson_model_template import show_model_page


def log_link(x):
    """Log link function for Poisson regression."""
    return np.log(x)

def exp_inverse_link(x):
    """Exponential inverse link function for Poisson regression."""
    return np.exp(x)

def show():
    st.markdown("""
    <h1 style='text-align: center;'>
        Making Sense of <span style='color: #ff9900;'>Counts</span> Without Losing Count with the help of <span style='color: #ff9900;'>GLMs</span>?
    </h1>
""", unsafe_allow_html=True)

    description = """
    As data scientists, we often find ourselves sifting through datasets filled with counts, such as the number of website visits, product sales, or even social media engagements. What is count data, you ask? Count data is simply the number of times an event will occur within a specific observation period or space. When it comes to counting data, choosing the right regression technique is pivotal. Many analysts would instinctively go for linear regression. But can multiple linear regression really handle count data? 
    """
    st.write(description)

    st.markdown("<hr style='border: none; border-top: 2px dashed gold;'>", unsafe_allow_html=True)

    more_description = """
    Let's answer a fundamental question, **Why not Linear regression**?
    1. Linear regression predicts real numbers including their negative forms. For count data that is rather silly; for example, can the number of birds visiting a garden ever consist of negative numbers? 
    2. Linear regression presumes that the residuals are distributed normally, which is not the case for count data where Poisson distribution does apply. 
    3. Finally, linear regression assumes constant variance. However, with count data, variance typically increases with the mean. For instance, if you observe birds for 1 hour, the number might range from 0 to 5, but if you observe for 10 hours, the range could expand to 10 to 50. This shows that the spread of data grows as the count increases, a pattern that linear regression can't accommodate. 
    """
    st.write(more_description)

    st.markdown("<hr style='border: none; border-top: 2px dashed gold;'>", unsafe_allow_html=True)

    conclusion = """
    **Solution? The Poisson Regression**.

    The Poisson, or rather link function, adjusts to count data with these limitations taken care of. Like other Generalized models, in Poisson regression the systematic component remains as Xβ. By taking log, the model expresses itself by means of the relationship that provides the log⁡(λ)=Xβ where, λ = expected count = E(Y),  X = predictor variables, and β = coefficients.
    This transformation guarantees that counts predicted will always be non-negative consistent with the essential properties of count data. 

    Wait…

    Does this not sound like a transformation in linear regression? The key difference is that a transformation changes the response or the predictor to match model assumptions, whereas in a link function, you apply the link to the mean of response rather than changing or transforming the actual response variable to accommodate the distribution of the response variable. 
    
    Some might suggest adding a constant to ensure the predictions are positive, but this approach oversimplifies the issue. It can lead to misleading results because it doesn't account for the structure of the data or its underlying distribution. Proper modeling is about more than just shifting values to make them fit.
    
    It is the natural choice for the need to model non-negative integers, coherent predictions, and the constraints induced from the model by the unique characteristics of the count data. The introduction of Poisson regression enables researchers and analysts to arrive at more accurate predictions and insights by recognizing Poisson Regression as a better model relative to traditional linear regression. Thus, it better propagates through analytics and research.
    """
    st.write(conclusion)

    st.write("Here is some Math Magic for you !")
    st.write("### (i) Fundamentals")
    st.latex(r"P(X = k) = \frac{e^{-\lambda}\lambda^k}{k!}")
    st.write("""
        This is the probability mass function of the Poisson distribution:
        - k is the number of occurrences (k = 0, 1, 2, ...)
        - λ > 0 is the average number of events in the interval
        - e is Euler's number (e ≈ 2.71828)
        """)
    st.write("### (ii) Generalized Linear Model for Poisson Regression")
    st.latex(r"Y \sim \text{Poisson}(\lambda)")
    st.latex(r"\eta = X\beta")
    st.latex(r"g(\mu) = \eta")
    st.write("""
        This structure defines Poisson regression as a GLM:
        - Y follows a Poisson distribution with mean λ
        - η = Xβ is the linear predictor (linear combination of predictors)
        - g(μ) is the link function connecting the expected value of Y (μ = λ) to the linear predictor
        """)
    st.write("### (iii) Log Link Function (Canonical Link)")
    st.latex(r"g(\mu) = \log(\mu) = \eta = X\beta")
    st.latex(r"\mu = e^{\eta} = e^{X\beta}")
    st.write("### (iv) Mean-Variance Relationship")
    st.latex(r"E(Y) = \text{Var}(Y) = \lambda")
    st.write("### (v) Interpretation of Coefficients")
    st.latex(r"e^{\beta_i} = \text{multiplicative change in } \mu \text{ for a one-unit increase in } x_i")
    st.latex(r"100(e^{\beta_i} - 1)\% = \text{percentage change in } \mu \text{ for a one-unit increase in } x_i")

    st.markdown("""
    <div>
        <span style='color: #ff9900; font-size: 20px; font-family: "Courier Prime", monospace;'>
            <em>Now, you know why Gamma prefers GLM over OLS—because it did not want to deal with normal drama!</em>
        </span>
    </div>
    """, unsafe_allow_html=True) 


    show_model_page("Poisson",
                    np.random.poisson,
                    log_link,
                    exp_inverse_link,
                    sm.families.Poisson()
                    )
