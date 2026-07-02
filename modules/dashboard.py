import pandas as pd
import streamlit as st


# ==========================================================
# DATASET SUMMARY
# ==========================================================

def show_summary(df, missing_analysis, duplicate_analysis, health_analysis):
    """
    Displays high-level dataset information.
    """

    st.header("📋 Dataset Summary")

    rows, cols = df.shape
    total_cells = rows * cols

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", f"{rows:,}")

    with col2:
        st.metric("Columns", f"{cols:,}")

    with col3:
        st.metric("Total Cells", f"{total_cells:,}")


# ==========================================================
# DATASET PREVIEW
# ==========================================================

def show_preview(df):
    """
    Displays first 10 rows of the dataset.
    """

    st.header("👀 Dataset Preview")

    st.dataframe(
        df.head(10),
        hide_index=True,
        use_container_width=True
    )


# ==========================================================
# COLUMN NAMES
# ==========================================================

def show_columns(df):
    """
    Displays all column names in a table.
    """

    st.header("📝 Column Names")

    column_df = pd.DataFrame({
        "Column Name": df.columns
    })

    st.dataframe(
        column_df,
        hide_index=True,
        use_container_width=True
    )


# ==========================================================
# DATA TYPES
# ==========================================================

def show_datatypes(df):
    """
    Displays data type of every column.
    """

    st.header("📌 Data Types")

    datatype_df = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(
        datatype_df,
        hide_index=True,
        use_container_width=True
    )