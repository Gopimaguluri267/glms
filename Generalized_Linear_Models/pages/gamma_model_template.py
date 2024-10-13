import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

def show_model_page(title, distribution_func, link_func, inverse_link_func):
    st.header("Model Visualization")
    
    col1, col2 = st.columns(2)
    with col1:
        n_samples = st.slider("Sample Size", min_value=100, max_value=10000, value=1000, step=100, key=f"{title}_sample_size")
    
    with col2:
        shape = st.slider("Shape Parameter (k)", min_value=0.1, max_value=10.0, value=2.0, step=0.1, key=f"{title}_shape")
        scale = st.slider("Scale Parameter (θ)", min_value=0.1, max_value=10.0, value=2.0, step=0.1, key=f"{title}_scale")


    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Distribution of Y")

        x = np.linspace(0.1, 10, n_samples)
        
        true_mean = shape * scale * (1 + 0.5 * x)
        y = distribution_func(shape, scale=true_mean / shape, size=n_samples)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(y, bins=30, kde=True, ax=ax, color='#8a2be2')
        font_properties = {'fontname': 'Courier New', 'fontsize': 18}
        ax.set_xlabel("Y (Response Variable)", fontdict=font_properties)
        ax.set_ylabel("Frequency", fontdict=font_properties)
        plt.xticks(fontname='Courier')
        plt.yticks(fontname='Courier')
        st.pyplot(fig)

    with col4:
        st.subheader("Gamma Regression Plot")
        
        X = sm.add_constant(x)
        
        model = sm.GLM(y, X, family=sm.families.Gamma(link=sm.families.links.log())).fit()
        
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x=x, y=y, alpha=0.5, label='Data', color='#ff9900', ax=ax)
        x_smooth = np.linspace(0.1, 10, 200)
        X_smooth = sm.add_constant(x_smooth)
        y_pred = model.predict(X_smooth)
        sns.lineplot(x=x_smooth, y=y_pred, color='#8a2be2', linewidth=2, label='Fitted Model', ax=ax)
        ax.set_xlabel("X (Predictor)")
        ax.set_ylabel("Y")
        plt.xticks(fontname='Courier')
        plt.yticks(fontname='Courier')
        ax.legend()
        st.pyplot(fig)

    with st.expander("Click to view the Model Summary"):

        st.markdown("""
        <div style='text-align: center;'>
            <h2 style='font-size: 24px;'>Model Summary</h2>
        </div>
        """, unsafe_allow_html=True)

        summary_model = model.summary()

        p1 = pd.DataFrame(summary_model.tables[0].data).loc[:, :1]
        p1.drop([5,6], inplace=True)
        p1.reset_index(drop=True, inplace=True)
        p1.columns= ["Metrics", "Values"]
        p2 = pd.DataFrame(summary_model.tables[0].data).loc[:, 2:]
        p2.drop([0], inplace=True)
        p2.reset_index(drop=True, inplace=True)
        p2.columns= ["Metrics", "Values"]
        model_info_df = pd.concat((p1, p2), axis=1)
        model_info_df.columns = ["Metrics", "Values", "Metrics", "Values"]
        model_info_df = model_info_df[:7]

        summary_df = pd.DataFrame(summary_model.tables[1].data[1:], columns=summary_model.tables[1].data[0])

        st.markdown("""
            <style>
            table {
                margin-left: auto;
                margin-right: auto;
                font-family: 'Courier New', monospace;
            }
            th, td {
                padding: 8px 12px;
                text-align: center;
            }
            </style>
            """, unsafe_allow_html=True)

        st.markdown(summary_df.to_html(index=False), unsafe_allow_html=True)

        st.markdown("""
            <style>
            table {
                margin-left: auto;
                margin-right: auto;
                font-family: 'Courier New', monospace;
            }
            th, td {
                padding: 8px 12px;
                text-align: center;
            }
            </style>
            """, unsafe_allow_html=True)

        st.markdown(model_info_df.to_html(index=False), unsafe_allow_html=True)
