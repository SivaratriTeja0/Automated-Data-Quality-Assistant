import streamlit as st

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

uploaded_file = st.file_uploader(
    "Upload your CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file:
    st.success(f"'{uploaded_file.name}' uploaded successfully!")

    st.button("Analyze My Data")