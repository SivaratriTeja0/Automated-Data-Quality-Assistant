import streamlit as st


def show_summary(df):

    st.header("📋 Dataset Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])


def show_preview(df):

    st.header("👀 Dataset Preview")

    st.dataframe(df.head(10), use_container_width=True)


def show_columns(df):

    st.header("📝 Column Names")

    st.write(list(df.columns))


def show_datatypes(df):

    st.header("📌 Data Types")

    datatype_df = df.dtypes.reset_index()

    datatype_df.columns = ["Column Name", "Data Type"]

    st.dataframe(datatype_df, use_container_width=True)


def show_missing(df):

    st.header("⚠ Missing Value Summary")

    missing_df = df.isnull().sum().reset_index()

    missing_df.columns = ["Column Name", "Missing Values"]

    missing_df = missing_df[
        missing_df["Missing Values"] > 0
    ]

    if missing_df.empty:

        st.success("✅ No Missing Values Found")

    else:

        st.dataframe(
            missing_df,
            use_container_width=True
        )