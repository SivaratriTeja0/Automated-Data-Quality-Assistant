import streamlit as st
import pandas as pd
from pathlib import Path

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Data Quality Assistant",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# Hero Section
# -------------------------------
st.title("📊 Data Quality Assistant")

st.subheader("Make Your Data Clean, Reliable & Ready to Use")

st.write("""
Welcome!

We help you identify and fix data quality issues in Excel and CSV files.

No coding required.
No technical knowledge required.

Simply upload your file and we'll guide you through the cleaning process.
""")

st.divider()

st.header("Why Use This Tool?")

col1, col2 = st.columns(2)

with col1:
    st.success("✔ Detect missing information")
    st.success("✔ Find duplicate records")
    st.success("✔ Standardize text")

with col2:
    st.success("✔ Identify incorrect data types")
    st.success("✔ Detect unusual values")
    st.success("✔ Download cleaned data")

st.divider()

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload your CSV or Excel file",
    type=["csv", "xlsx"]
)

# -------------------------------
# Read Uploaded File
# -------------------------------
if uploaded_file is not None:

    try:
        # Get filename and extension
        filename = uploaded_file.name
        extension = Path(filename).suffix.lower()

        # Read file based on extension
        if extension == ".csv":
            df = pd.read_csv(uploaded_file)

        elif extension == ".xlsx":
            df = pd.read_excel(uploaded_file)

        else:
            st.error("❌ Unsupported file type.")
            st.stop()

        # Success Message
        st.success(f"✅ '{filename}' uploaded successfully!")

        # Dataset Information
        st.subheader("📋 Dataset Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        st.write("### 👀 Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

    except Exception as e:
        st.error("❌ Unable to read the uploaded file.")
        st.error(f"Error: {e}")