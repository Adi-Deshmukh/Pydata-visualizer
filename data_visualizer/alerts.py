from typing import Dict, List, Optional
from .settings import Settings
import pandas as pd

def generate_alerts(column_details: Dict, settings: Optional[Settings] = None) -> List[Dict]:
    """
    Generate data quality alerts for a column based on its statistics.
    """
    alerts = []
    skewness_threshold = 1.0 if settings is None else settings.skewness_threshold

    skewness = column_details.get("skewness")
    if skewness is not None and not pd.isna(skewness) and abs(skewness) > skewness_threshold:
        alerts.append({
            "alert_type": "skewness",
            "message": f"Data is highly skewed (value: {skewness:.2f})",
            "value": skewness
        })

    missing_percent = column_details.get("missing_%")
    if missing_percent is not None and missing_percent > 20:
        alerts.append({
            "alert_type": "High Missing Values",
            "message": f"Data is highly missing (value: {missing_percent:.2f}%)",
            "value": missing_percent
        })

    outlier_count = column_details.get("outlier_count")
    outlier_percentage = column_details.get("outlier_percentage")
    if outlier_count is not None and outlier_count > 0:
        alerts.append({
            "alert_type": "Outliers",
            "message": f"Outliers detected: {outlier_count} ({outlier_percentage:.2f}%)",
            "value": outlier_count
        })

    return alerts

def generate_dataset_alerts(dataset_details: Dict, settings: Optional[Settings] = None) -> List[Dict]:

    alerts = []
    duplicate_threshold = 5.0 if settings is None else settings.duplicate_threshold

    duplicate_percentage = dataset_details.get("duplicate_percentage")
    if duplicate_percentage is not None and duplicate_percentage > duplicate_threshold:
        alerts.append({
            "alert_type": "High Duplicates",
            "message": f"High duplicate rate: {duplicate_percentage:.2f}%",
            "value": duplicate_percentage
        })

    return alerts