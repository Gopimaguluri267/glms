import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pages.gamma_model_template import show_model_page


def show():
    st.markdown("""
    <h1 style='text-align: center;'>
        Modelling The  <span style='color: #ff9900;'>Rubber Band</span> of Distributions
    </h1>
""", unsafe_allow_html=True)

    description = """
    Some (Most, if you ask us) data in today's world do not follow the ideal "Normal Distribution" (the bell shaped curve). Instead, data are often continuous, strictly positive and skewed, with long tails and big humps to the side. Think about methane emissions from an oil and gas plant, life expectancy of machines, income and expenditure of households, and even the infamously long wait times at the doctor's office. All these are examples of variables that follow something called the "Gamma Distribution" and are better modeled with a different approach, beyond the standard linear regression. 

    Firstly, let's get a sense of what the "Gamma Distribution" is. 

    The gamma distribution is like a blob of clay that can be shaped in multiple ways based on two important factors. Let the first factor be the *"stretchiness"* which represents the width of the hump/bump you make with the clay. Higher the stretchiness, the wider the hump, and the second factor is the *"twistiness"*, which represents the length of the tail of the humps. 
    Statistically speaking, the factors are the parameters of the distribution (gamma in our case) of the underlying variable. The factor *"stretchiness"* is called the scale parameter represented by beta and the *"twistiness"* factor is called the shape parameter represented by alpha. *Very Interestingly, the mean and variance of the target variable (the variable following the gamma distribution) is given by: $\\alpha \\cdot \\beta$ and $\\alpha \\cdot \\beta^2$*
    """

    st.write(description)

    st.markdown("<hr style='border: none; border-top: 2px dashed gold;'>", unsafe_allow_html=True)

    more_description = """
    Now, answering the most important question…why can't we just use Ordinary Least Squares (OLS) regression (the regular linear modeling)?
    
    The obvious point is that for OLS, our target variable needs to follow a normal distribution, and Gamma isn't normal (pun intended again!). Target variables, like waiting time at a hospital, income, and methane emissions, are always positive and cannot be negative. The OLS regression line extends both ways, in the positive and negative direction, which means you can sometimes predict illogical outcomes like negative time and income.
    
    Thirdly, OLS assumes that the variance is constant across all levels of the predictor, whereas the gamma distribution has varying variance depending on the mean.
    
    Now, you might wonder, why can't we just simply transform the target variable to a form that is convenient for us? Yes! We can, but at what cost? We lose a lot of information when non-normal data is transformed, complicating interpretation. Instead, we model the mean of the distribution using a link function.

    For the gamma distribution, there are several link functions we can use:
    
    - **Log Link Function**: Suitable when the data is right-skewed (i.e., it has a long tail on the right with the hump/bump on the left).
    - **Inverse Link Function**: Used when the average value of the target variable decreases with an increase in the predictor variable. For example, the increase in average take-home salary (the target) may diminish with higher income tax (the predictor).
    - **Square Root Link Function**: Useful when variance is proportional to the mean, helping to model diminishing returns. This is mostly applied in ecological and biological contexts.
    """

    st.write(more_description)

    st.markdown("<hr style='border: none; border-top: 2px dashed gold;'>", unsafe_allow_html=True)

    conclusion = """
    How does the GLM work with the Gamma Distribution? 

    Very simply, the expected value of the target variable is modeled to a linear predictor. Instead of modeling the mean ($$\\mu$$) directly, we model a function of $$\\mu$$ to the linear predictor. This function is usually one among the three link functions discussed above, chosen based on data and context.

    The parameters of the linear predictor are estimated through the maximum likelihood estimation technique (MLE). This optimization is carried out numerically, and the best linear predictor is found. Given new data points from the predictors, we estimate $$\\mu$$ using the model we created.

    Next, we determine the probability density function (PDF) of the distribution (Gamma, in our case) using the modeled mean and the sample variance. This PDF is found by comparing the mean and variance and using the so-called "Interesting fact" discussed earlier (the mean and variance of the target variable following gamma distribution is given by $$ \\alpha \\cdot \\beta $$ and $$ \\alpha \\cdot \\beta^2 $$, respectively).

    Finally, we estimate our target variable (variable of interest) using this PDF. 
    """

    st.write(conclusion)
    st.write("Here is some Math Magic !")
    st.write("### (i) Fundamentals")
    st.latex(r"f(x; \alpha, \theta) = \frac{x^{\alpha - 1}e^{-x/\theta}}{\theta^\alpha \Gamma(\alpha)}")
    st.write("""
        This is the probability density function (PDF) of the Gamma distribution:
        - x is the continuous random variable (x > 0)
        - α > 0 is the shape parameter
        - θ > 0 is the scale parameter
        - Γ(α) is the Gamma function, a generalization of the factorial
        """)
    st.write("### (ii) Generalized Linear Model for Gamma Regression")
    st.latex(r"Y \sim \text{Gamma}(\alpha, \theta)")
    st.latex(r"\eta = X\beta")
    st.latex(r"g(\mu) = \eta")
    st.write("""
        This structure defines Gamma regression as a GLM:
        - Y follows a Gamma distribution with shape parameter α and scale parameter θ
        - η = Xβ is the linear predictor (linear combination of predictors)
        - g(μ) is the link function connecting the expected value of Y (μ) to the linear predictor
        """)
    st.write("### (iii) Inverse Link Function (Canonical Link)")
    st.latex(r"g(\mu) = \frac{1}{\mu} = \eta = X\beta")
    st.latex(r"\mu = \frac{1}{\eta} = \frac{1}{X\beta}")
    st.write("### (iv) Mean-Variance Relationship")
    st.latex(r"\text{Var}(Y) = \mu^2 / \alpha")
    st.write("### (v) Interpretation of Coefficients")
    st.latex(r"\frac{\partial \mu}{\partial x_i} = -\frac{\mu^2}{X\beta} \cdot \beta_i")
    st.write("""
    In Gamma regression, the relationship between the predictors $$X$$ and the expected value of the response $$\\mu$$ is nonlinear. 
    The rate of change in $$\\mu$$ due to a one-unit increase in the predictor $$x_i$$ depends on both the current value of $$\\mu$$ and the coefficients $$\\beta_i$$.

    - If $$\\beta_i > 0$$, $$\\mu$$ decreases as $$x_i$$ increases.
    - If $$\\beta_i < 0$$, $$\\mu$$ increases as $$x_i$$ increases.

    The effect of a one-unit increase in $$x_i$$ on $$\\mu$$ is multiplicative:
    - $$e^{\\beta_i}$$ gives the multiplicative change in $$\\mu$$ for a one-unit increase in $$x_i$$.
    - For example, if $$\\beta_i = 0.1$$, a one-unit increase in $$x_i$$ would increase $$\\mu$$ by approximately 10.5% (since $$e^{0.1} \\approx 1.105$$).
    - If $$\\beta_i = -0.2$$, a one-unit increase in $$x_i$$ would decrease $$\\mu$$ by about 18.2% (since $$e^{-0.2} \\approx 0.818$$).
""")

    st.markdown("""
    <div>
        <span style='color: #ff9900; font-size: 20px; font-family: "Courier Prime", monospace;'>
            <em>Now, you know why Gamma prefers GLM over OLS—because it did not want to deal with normal drama!</em>
        </span>
    </div>
    """, unsafe_allow_html=True)    
    
    show_model_page("Gamma_Regression",
                     np.random.gamma,
                     np.log,
                     np.exp)
