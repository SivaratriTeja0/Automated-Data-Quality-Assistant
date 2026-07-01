import streamlit as st

from modules.loader import load_file

from modules.dashboard import (
    show_summary,
    show_preview,
    show_columns,
    show_datatypes
)

from modules.quality import (
    analyze_missing_values,
    analyze_duplicates,
    calculate_health_score
)

# ==========================================================
# PAGE CONFIGURATION
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

st.markdown("""
Ensure your data is **accurate, complete and analysis-ready**
before making business decisions.

This application helps you detect, understand and resolve
common data quality issues in CSV and Excel datasets without
requiring programming knowledge.
""")

st.divider()

# ==========================================================
# HOW WE HELP YOU
# ==========================================================

st.header("🚀 How We Help You")

col1, col2 = st.columns(2)

with col1:

    st.success("📂 Upload CSV or Excel datasets")

    st.success("📊 Analyze dataset health")

    st.success("🔍 Detect quality issues")

    st.success("💡 Get intelligent recommendations")

with col2:

    st.success("🧹 Clean datasets automatically")

    st.success("📄 Generate quality reports")

    st.success("📥 Download cleaned datasets")

    st.success("📈 Build confidence in your data")

st.divider()

# ==========================================================
# HOW IT WORKS
# ==========================================================

st.header("📋 How It Works")

st.markdown("""
### Step 1
📂 Upload your CSV or Excel dataset.

### Step 2
🔍 Our Quality Engine scans your dataset.

### Step 3
📊 Review health score, missing values,
duplicates and quality issues.

### Step 4
🧹 Clean and download your dataset.
""")

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

        # -----------------------------------------
        # Load Dataset
        # -----------------------------------------

        df, filename, extension = load_file(uploaded_file)

        st.success(f"✅ {filename} uploaded successfully!")

        # -----------------------------------------
        # Dashboard
        # -----------------------------------------

        show_summary(df)

        # -----------------------------------------
        # Quality Analysis
        # -----------------------------------------

        missing_analysis = analyze_missing_values(df)

        duplicate_analysis = analyze_duplicates(df)

        health_analysis = calculate_health_score(
            missing_analysis,
            duplicate_analysis
        )

        # -----------------------------------------
        # Tabs
        # -----------------------------------------

        tab1, tab2, tab3 = st.tabs([
            "👀 Preview",
            "📊 Dashboard",
            "🔍 Quality Report"
        ])

        # =========================================
        # PREVIEW TAB
        # =========================================

        with tab1:

            show_preview(df)

        # =========================================
        # DASHBOARD TAB
        # =========================================

        with tab2:

            show_columns(df)

            st.divider()

            show_datatypes(df)

        # =========================================
        # QUALITY REPORT TAB
        # =========================================

        with tab3:

            st.subheader("📊 Dataset Health")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Health Score",
                    f"{health_analysis['health_score']}%"
                )

            with col2:

                st.metric(
                    "Quality Rating",
                    health_analysis["rating"]
                )

            st.divider()

            st.subheader("🔍 Quality Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Missing Values",
                    missing_analysis["total_missing"]
                )

            with col2:

                st.metric(
                    "Duplicate Rows",
                    duplicate_analysis["duplicate_count"]
                )

            col3, col4 = st.columns(2)

            with col3:

                st.metric(
                    "Missing %",
                    f"{missing_analysis['missing_percentage']}%"
                )

            with col4:

                st.metric(
                    "Duplicate %",
                    f"{duplicate_analysis['duplicate_percentage']}%"
                )

            st.divider()

            st.subheader("📋 Missing Values by Column")

            missing_df = (
                missing_analysis["missing_by_column"]
                .reset_index()
            )

            missing_df.columns = [
                "Column Name",
                "Missing Values"
            ]

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

            st.info("""
💡 Recommendation

Review the affected columns before performing
analysis or building dashboards.

Missing values can lead to incorrect business
insights and inaccurate machine learning models.
""")

            if duplicate_analysis["duplicate_count"] == 0:

                st.success("✅ Dataset contains no duplicate records.")

            else:

                st.warning(
                    f"⚠ {duplicate_analysis['duplicate_count']} duplicate rows detected."
                )

    except Exception as e:

        st.error("❌ Unable to process the uploaded file.")

        st.error(str(e))