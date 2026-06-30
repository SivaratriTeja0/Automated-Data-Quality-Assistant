import pandas as pd
from pathlib import Path


def load_file(uploaded_file):
    """
    Reads uploaded CSV or Excel file
    Returns:
        DataFrame
        File Name
        Extension
    """

    filename = uploaded_file.name
    extension = Path(filename).suffix.lower()

    if extension == ".csv":
        df = pd.read_csv(uploaded_file)

    elif extension == ".xlsx":
        df = pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported File Type")

    return df, filename, extension