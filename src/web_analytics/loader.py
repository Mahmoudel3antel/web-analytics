import os

import pandas as pd


REQUIRED_COLUMNS = {
    "timestamp",
    "session_id",
    "page",
    "country",
    "device",
    "duration",
}


def load_data(file_path):
    """Load and validate website analytics data from a CSV file."""

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    data = pd.read_csv(file_path)

    if data.empty:
        raise ValueError("The dataset is empty.")

    missing_columns = REQUIRED_COLUMNS - set(data.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    data["timestamp"] = pd.to_datetime(data["timestamp"])

    data["duration"] = pd.to_numeric(
        data["duration"],
        errors="coerce",
    )

    return data