import streamlit as st

def app():
    # st.set_page_config(page_title="HomeMatch", page_icon="🏠")
    st.title("🏠 HomeWorth Philly: Your Property's Value, Just a Click Away")

    st.markdown("""
    ## 🏙️ About HomeWorth Philly
    ---
    **HomeWorth Philly** is a machine learning–powered solution platform for predicting residential property prices in Philadelphia to generate fair price estimates based on key property characteristics.

    ## 🧠 Core Business Problem

    Traditional approaches rely heavily on:
    - **Outdated transaction data** (limited to 2017–2018)
    - **Multiple Linear Regression**
        Struggles to capture non-linear relationships, especially with large and complex datasets
    - **Manual human intervention**, which introduces bias and inconsistency

    These factors lead to:
    - Mispriced properties  
    - Flawed housing policy decisions  
    - Inefficient tax assessments  

    ---

    ## ✅ Our Modern Approach (UNDER DEVELOPMENT)

    We address this with a **modern ML-based mass appraisal system** using:
    - **Tree Based Regressor** — state-of-the-art, powerful models designed for both linear and non-linear data, and optimized for large datasets
    - Extended dataset up to **2020**
    - Systematic **feature engineering and EDA**
    - **Inferential comparisons** between market value and sale price
    - **Model interpretability** via AI Powered

    ---

    ## 📊 Model Performance (UNDER DEVELOPMENT)

    The model evaluated on previously unseen property data, it delivered **strong generalization**:

    - 🧠 The model can explain over **94% of the variance** in market values. Solid predictive power.

    - 💵 On average, the model’s predictions are off by **around $13K** — a practical range for most urban properties.

    - 📊 The typical prediction error is **just under 10%**, making it reliable for real-world decisions.

    - 📉 Larger deviations are rare but can reach up to **$39K** — a signal that outlier handling matters.

    The model performs confidently across typical properties, with robust accuracy and manageable risk for mispricing.
    

    🔍 **Most impactful features**: (UNDER DEVELOPMENT)
        `total livable area`, `total area`, `interior condition`, `location`

    ---

    ## 📌 Why HomeMatch Matters (UNDER DEVELOPMENT)

    Accurate residential valuation helps:
    - 🏘️ **Homeowners** price competitively  
    - 💰 **Buyers & lenders** make informed decisions  
    - 🏦 **City governments** ensure fair taxation 
    - 📈 **Investors** spot opportunities  

    > Accurate mass prediction = better policy, fairer pricing, smarter investment.

    ---

    ## 📐 Analytic Framework (UNDER DEVELOPMENT)

    - 🔍 **EDA & Feature Engineering** on structured residential data
    - 🧠 **Machine Learning Regression** (Random Forest) to predict market value
    - 🔬 **Model evaluation**: RMSE, MAE, MAPE, R²
    - 📉 **Error Analysis** between market value and predicted market value
    - 📌 **Interpretability** via AI Powered
    
    ---

    ## 🎯 Goal (UNDER DEVELOPMENT)
    > **"Build an accurate, automated, and fair house pricing system predictor using machine learning to support smart real estate decision-making and improve pricing accuracy across Philadelphia."**

    Ready to predict smarter? Use the sidebar and get started.
    """)

    st.markdown(
        '<p style="font-size: 10px; color: gray;">Developed by the Data Science Team at the Housing Association of Philadelphia (HAP)</p>',
        unsafe_allow_html=True
    )
if __name__ == "__main__":
    app()
