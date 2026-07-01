"""
==========================================================
Data Quality Assistant
Quality Analysis Module
==========================================================

This module is responsible for analyzing dataset quality.

Current Features
----------------
✔ Missing Value Analysis
✔ Duplicate Row Analysis
✔ Dataset Health Score

Future Features
---------------
□ Blank String Detection
□ Email Validation
□ Phone Number Validation
□ Date Format Validation
□ Data Type Validation
□ Outlier Detection (IQR)
□ Negative Value Detection
"""

# ==========================================================
# MISSING VALUE ANALYSIS
# ==========================================================

def analyze_missing_values(df):
    """
    Analyze missing values in the dataset.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict
    """

    missing_by_column = df.isnull().sum()

    total_missing = int(missing_by_column.sum())

    missing_percentage = round(
        (total_missing / (df.shape[0] * df.shape[1])) * 100,
        2
    ) if df.shape[0] * df.shape[1] != 0 else 0

    return {

        "total_missing": total_missing,

        "missing_percentage": missing_percentage,

        "missing_by_column": missing_by_column

    }


# ==========================================================
# DUPLICATE ANALYSIS
# ==========================================================

def analyze_duplicates(df):
    """
    Analyze duplicate rows.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict
    """

    duplicate_rows = df[df.duplicated()]

    duplicate_count = len(duplicate_rows)

    duplicate_percentage = round(
        (duplicate_count / df.shape[0]) * 100,
        2
    ) if df.shape[0] != 0 else 0

    return {

        "duplicate_count": duplicate_count,

        "duplicate_percentage": duplicate_percentage,

        "duplicate_rows": duplicate_rows

    }


# ==========================================================
# HEALTH SCORE
# ==========================================================

def calculate_health_score(*analysis_results):
    """
    Calculate dataset health score.

    Accepts any number of analysis dictionaries.

    Example
    -------
    calculate_health_score(
        missing_analysis,
        duplicate_analysis
    )

    Future
    ------
    calculate_health_score(
        missing_analysis,
        duplicate_analysis,
        blank_analysis,
        email_analysis,
        phone_analysis,
        ...
    )
    """

    quality_loss = 0

    for analysis in analysis_results:

        for key, value in analysis.items():

            if key.endswith("_percentage"):

                quality_loss += value

    health_score = max(
        0,
        round(100 - quality_loss, 2)
    )

    if health_score >= 95:

        rating = "🟢 Excellent"

    elif health_score >= 80:

        rating = "🟡 Good"

    elif health_score >= 60:

        rating = "🟠 Needs Cleaning"

    else:

        rating = "🔴 Poor"

    return {

        "health_score": health_score,

        "quality_loss": round(quality_loss, 2),

        "rating": rating

    }