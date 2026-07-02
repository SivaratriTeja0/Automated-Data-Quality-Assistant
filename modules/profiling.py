import pandas as pd
import streamlit as st


# ==========================================================
# DATASET SHAPE
# ==========================================================

def dataset_shape(df):
    """
    Displays dataset shape information.
    """

    rows, cols = df.shape
    total_cells = rows * cols

    st.subheader("📊 Dataset Shape")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", f"{rows:,}")

    with col2:
        st.metric("Columns", f"{cols:,}")

    with col3:
        st.metric("Total Cells", f"{total_cells:,}")


# ==========================================================
# MEMORY USAGE
# ==========================================================

def memory_usage(df):
    """
    Displays dataset memory usage.
    """

    memory = df.memory_usage(deep=True).sum()

    if memory < 1024:
        size = f"{memory:.2f} Bytes"

    elif memory < 1024 ** 2:
        size = f"{memory / 1024:.2f} KB"

    elif memory < 1024 ** 3:
        size = f"{memory / (1024 ** 2):.2f} MB"

    else:
        size = f"{memory / (1024 ** 3):.2f} GB"

    st.subheader("💾 Memory Usage")
    st.metric("Dataset Size", size)


# ==========================================================
# NUMERIC SUMMARY
# ==========================================================

def numeric_summary(df):
    """
    Displays summary statistics for numeric columns.
    """

    numeric_df = df.select_dtypes(include="number")

    st.subheader("📈 Numeric Column Summary")

    if numeric_df.empty:
        st.info("No numeric columns found.")
        return

    summary = pd.DataFrame({
        "Mean": numeric_df.mean(),
        "Median": numeric_df.median(),
        "Minimum": numeric_df.min(),
        "Maximum": numeric_df.max(),
        "Std Dev": numeric_df.std(),
        "Missing Values": numeric_df.isnull().sum()
    })
    summary = summary.reset_index()
    summary.columns = [
    "Column Name",
    "Mean",
    "Median",
    "Minimum",
    "Maximum",
    "Std Dev",
    "Missing Values"
    ]
    hide_index=True,
    use_container_width=True
    st.dataframe(summary.round(2))


# ==========================================================
# CATEGORICAL SUMMARY
# ==========================================================

def categorical_summary(df):
    """
    Displays summary statistics for categorical columns.
    """

    categorical_df = df.select_dtypes(include=["object", "category"])

    st.subheader("📝 Categorical Column Summary")

    if categorical_df.empty:
        st.info("No categorical columns found.")
        return

    summary = []

    for column in categorical_df.columns:

        top = categorical_df[column].mode(dropna=True)

        if len(top) > 0:
            top_value = top.iloc[0]
            frequency = categorical_df[column].value_counts().iloc[0]
        else:
            top_value = "N/A"
            frequency = 0

        summary.append({
            "Column": column,
            "Unique Values": categorical_df[column].nunique(dropna=True),
            "Most Common Value": top_value,
            "Frequency": frequency,
            "Missing Values": categorical_df[column].isnull().sum()
        })

    st.dataframe(pd.DataFrame(summary), 
                 hide_index=True, 
                 use_container_width=True)


# ==========================================================
# UNIQUE VALUE ANALYSIS
# ==========================================================

def unique_values(df):
    """
    Displays unique value statistics for every column.
    """

    st.subheader("🔍 Unique Value Analysis")

    summary = []

    total_rows = len(df)

    for column in df.columns:

        unique = df[column].nunique(dropna=True)

        if total_rows == 0:
            unique_percent = 0
        else:
            unique_percent = (unique / total_rows) * 100

        summary.append({
            "Column": column,
            "Unique Values": unique,
            "Unique %": round(unique_percent, 2)
        })

    st.dataframe(pd.DataFrame(summary), 
                 hide_index=True, 
                 use_container_width=True)


# ==========================================================
# COMPLETE PROFILING
# ==========================================================

def show_profiling(df):
    """
    Runs the complete profiling report.
    """

    st.header("📋 Dataset Profiling")

    dataset_shape(df)

    st.divider()

    memory_usage(df)

    st.divider()

    numeric_summary(df)

    st.divider()

    categorical_summary(df)

    st.divider()

    unique_values(df)