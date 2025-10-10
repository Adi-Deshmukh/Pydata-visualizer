import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64
import warnings
from typing import List, Optional

# Set global font for wider character support
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Verdana']

"""
    Generates a plot for a pandas Series, saves it to a memory buffer,
    and returns it as a Base64-encoded PNG for HTML embedding.
    Highlights outliers in numeric histograms.

    Args:
        column_data: pandas Series to plot
        column_name: Name of the column for title
        outliers: List of outlier values (for numeric columns)

    Returns:
        Base64-encoded PNG data URL
    """

def get_plot_as_base64(column_data: pd.Series, column_name: str, outliers: Optional[List] = None) -> str:

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
        plt.figure(figsize=(6, 4))
        plt.style.use('seaborn-v0_8-whitegrid')

        if pd.api.types.is_numeric_dtype(column_data):
            if outliers is not None:
                inliers = column_data[~column_data.isin(outliers)]
                sns.histplot(inliers, kde=True, bins=20, color="#17a2b8", label='Inliers')
                if outliers:
                    sns.histplot(outliers, kde=False, bins=20, color="#dc3545", alpha=0.5, label='Outliers')
                plt.legend()
            else:
                sns.histplot(column_data, kde=True, bins=20, color="#17a2b8")
            plt.title(f'Distribution of {column_name}')
        else:
            top_10 = column_data.value_counts().nlargest(10)
            clean_labels = [str(label).replace('$', '\\$').replace('_', '\\_') for label in top_10.index]
            sns.barplot(x=clean_labels, y=top_10.values, palette="viridis")
            plt.title(f'Top 10 Values for {column_name}')
            plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        plt.close()
        data = base64.b64encode(buf.getbuffer()).decode('ascii')
        return f"data:image/png;base64,{data}"