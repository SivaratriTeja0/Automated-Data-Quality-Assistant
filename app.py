import streamlit as st

from modules.loader import load_file

from modules.dashboard import (
    show_summary,
    show_preview,
    show_columns,
    show_datatypes,
    show_missing
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Data Quality Assistant",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# HEADER
# ==========================================================

st.title("📊 Data Quality Assistant")

st.subheader("Upload. Analyze. Clean. Trust Your Data.")

st.write("""
Welcome!

Upload your CSV or Excel dataset and let Data Quality Assistant
analyze its quality before you start your analysis.
""")

st.divider()

# ==========================================================
# FEATURES
# ==========================================================

st.header("Why Use This Tool?")

col1, col2 = st.columns(2)

with col1:
    st.success("✔ Detect Missing Values")
    st.success("✔ Find Duplicate Records")
    st.success("✔ Validate Data Types")

with col2:
    st.success("✔ Detect Outliers")
    st.success("✔ Generate Reports")
    st.success("✔ Download Cleaned Data")

st.divider()

# ==========================================================
# FILE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "📂 Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

# ==========================================================
# MAIN APPLICATION
# ==========================================================

if uploaded_file is not None:

    try:

        df, filename, extension = load_file(uploaded_file)

        st.success(f"✅ {filename} uploaded successfully!")

        show_summary(df)

        st.divider()

        tab1, tab2, tab3, tab4 = st.tabs([
            "👀 Preview",
            "📝 Columns",
            "📌 Data Types",
            "⚠ Missing Values"
        ])

        with tab1:
            show_preview(df)

        with tab2:
            show_columns(df)

        with tab3:
            show_datatypes(df)

        with tab4:
            show_missing(df)

    except Exception as e:

        st.error("❌ Unable to read uploaded file.")

        st.error(e)