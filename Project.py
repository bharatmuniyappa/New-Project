#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="General Dataset Analyzer", layout="wide")
st.title("📊 General Dataset Analyzer & Code Generator")

# 1. File Upload
uploaded_file = st.file_uploader("Upload your dataset (CSV only)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")

    # 2. Dataset Preview
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head())

    # 3. Data Summary
    st.subheader("📈 Summary Statistics")
    st.write(df.describe(include='all'))

    # 4. Missing Value Report
    st.subheader("❗ Missing Values")
    st.write(df.isnull().sum())

    # 5. Data Types
    st.subheader("📂 Data Types")
    st.write(df.dtypes)

    # 6. Correlation Heatmap
    st.subheader("🔗 Correlation Heatmap")
    numeric_df = df.select_dtypes(include='number')
    if not numeric_df.empty:
        fig, ax = plt.subplots()
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    else:
        st.info("No numeric columns for correlation analysis.")

    # 7. Histograms for Numeric Columns
    st.subheader("📊 Histograms (Numeric Columns)")
    if not numeric_df.empty:
        fig = numeric_df.hist(figsize=(12, 8))
        st.pyplot(fig[0][0].get_figure())
    else:
        st.info("No numeric columns to plot histograms.")

    # 8. Auto-Generated Analysis Code
    st.subheader("🧠 Auto-Generated Python Code")

    generated_code = f"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("your_dataset.csv")

# Preview
print(df.head())

# Summary
print(df.describe(include='all'))

# Missing values
print(df.isnull().sum())

# Data types
print(df.dtypes)

# Correlation heatmap
numeric_df = df.select_dtypes(include='number')
if not numeric_df.empty:
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

# Histograms
if not numeric_df.empty:
    numeric_df.hist(figsize=(12, 8))
    plt.tight_layout()
    plt.show()
"""

    st.code(generated_code, language='python')

    # 9. Code Download Option
    code_file = io.StringIO(generated_code)
    st.download_button("📥 Download Code", code_file, file_name="auto_analysis_code.py", mime="text/x-python")


# In[ ]:




