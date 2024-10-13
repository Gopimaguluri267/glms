import streamlit as st
import numpy as np
from scipy.special import expit
from pages.logistic_model_template import show_model_page

def show():

    st.markdown("""
    <h1 style='text-align: center;'>
        Is it <span style='color: #ff9900;'>Cat</span> or <span style='color: #ff9900;'>Dog</span>?
    </h1>
""", unsafe_allow_html=True)

    description = """
    When faced with the challenge of predicting outcomes that fall into distinct categories, what will you do? At this point, you might scratch your head and ask yourself, "Why can't I just run a linear regression on that?" And, in fact, it's a very frequent question. The answer has something to do with the nature of binary data. That is, linear regression assumes a continuous outcome, and the relationship between independent and dependent variables is linear. However, binary outcomes obviously violate this assumption. For instance, it doesn't make sense to predict a probability of $$-0.2$$ on a yes/no response.

    Also, linear regression assumes that residuals (i.e., the differences between what is observed and predicted) are normally distributed. In binary data, this is not the case, since the resulting probabilities are nowhere near normal. Besides being illogical, the resulting predictions with linear regression are unreliable.

    So GLMs present the solution. Logistic regression addresses these issues with elegance. The method curves the linear combination of the predictors within the range from 0 to 1 and writes out the probability directly. Mathematically speaking, the probability of logistic regression can be expressed as follows:
    $$ P(Y=1) = \\frac{1}{1 + e^{-X\\beta}} $$

    Where, $P(Y=1)$ is the probability of occurrence of an event, say a purchase, $$(X)$$ represents predictor variables like age, income, and so on, and $$\\beta$$ are the coefficients learned by the model from the data.
    """

    st.write(description)

    st.markdown("<hr style='border: none; border-top: 2px dashed gold;'>", unsafe_allow_html=True)

    more_description = """
    First, the important property of the logistic function is that it forms an S-shaped curve, important for the correct interpretation of the probabilities. While the value of the predictor increases, the predicted probability approaches 1; with a decrease, it goes toward 0. This property ensures that the predictions fall within a valid range of probabilities and correctly reflect the nature of binary outcomes.

    Logistic regression is a rich source of insight, not just the mere prediction of an outcome. It comes out through the way coefficients, $$\\beta$$, can be interpreted in terms of odds ratios from the model, hence giving an explicit picture of how changes in predictor variables affect the likelihood of the outcome. For example, if a coefficient of 0.5 on a predictor variable implies that for every one-unit increase in the variable, there is an approximate increase by 65% in the odds of the occurrence of the event: $$ e^{0.5} \\approx 1.65 $$

    This interpretability makes logistic regression one of the most common machine learning algorithms used in healthcare, marketing, and social sciences, to name a few. It offers a way where analysts or researchers can drive home findings rather effectively and make decisions based on data.
    """

    st.write(more_description)

    st.markdown("<hr style='border: none; border-top: 2px dashed gold;'>", unsafe_allow_html=True)

    conclusion = """
    Logistic regression models binary outcomes. It does this by taking the linear combinations of predictors into probabilities in a way that is meaningful, with good interpretability. This makes it an excellent go-to option among many analysts. Perhaps most tempting, reaching out by habit for linear regression is to recognize limitations, and these are keys to success in data analysis.
    
    So, the next time there is a binary outcome in your data, remember the power of logistic regression. Leverage that power to provide not just predictions but deep insights into the story that your data tells. Happy analyzing!
    """

    st.write(conclusion)

    st.write("Here is some Math Magic for you !")
    st.write("### (i) Fundamentals")
    st.latex(r"\sigma(z) = \frac{1}{1 + e^{-z}}")
    st.write("""
    This is the sigmoid function, fundamental to logistic regression:
    - It is the ‘S’ shaped curve we discussed in the beginning of the section.
    - You can see this in the graphs at the end of the page.
    """)
    st.write("### (ii) The Structure")
    st.latex(r"Y \sim \text{Bernoulli}(p) \text{ or } Y \sim \text{Binomial}(n, p)")
    st.latex(r"\eta = X\beta")
    st.latex(r"g(p) = \eta")
    st.write("""
    This structure defines logistic regression as a GLM:
    - Y follows a Bernoulli distribution (for binary outcomes) or Binomial (for proportion data).
    - η = Xβ is the linear combination of predictors.
    - The link function g(p) connects the expected value of Y (p) to the linear predictor.
    """)
    st.write("### (iii) Logit Link Function (Canonical Link)")
    st.latex(r"g(p) = \log\left(\frac{p}{1-p}\right) = \eta = X\beta")
    st.latex(r"p = \frac{e^{\eta}}{1 + e^{\eta}} = \frac{1}{1 + e^{-\eta}}")
    st.write("### (iv) Odds and Odds Ratio")
    st.latex(r"\text{odds} = \frac{p}{1-p} = e^{\eta} = e^{X\beta}")
    st.latex(r"\text{OR} = e^{\beta_i}")
    st.write("### (v) Interpretation of Coefficients")
    st.latex(r"e^{\beta_i} = \text{odds ratio for a one-unit increase in } x_i")
    st.latex(r"100(e^{\beta_i} - 1)\% = \text{percentage change in odds for a one-unit increase in } x_i")

    show_model_page("Logistic Regression",
        lambda x: np.random.binomial(1, expit(x-0.5)),
        lambda x: np.log(x / (1 - x)),
        expit
    )
