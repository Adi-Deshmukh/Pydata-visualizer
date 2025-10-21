# Pydata-visualizer User Guide

This guide provides a step-by-step introduction to using the Pydata-visualizer library for data analysis and profiling.

## Table of Contents

1. [Installation](#1-installation)
2. [Basic Usage](#2-basic-usage)
3. [Understanding the Report](#3-understanding-the-report)
4. [Advanced Configuration](#4-advanced-configuration)
5. [Working with Large Datasets](#5-working-with-large-datasets)
6. [Common Use Cases](#6-common-use-cases)
7. [Customization Options](#7-customization-options)

## 1. Installation

### Using pip

```bash
pip install pydata-visualizer
```

### Verifying Installation

You can verify the installation was successful by importing the library:

```python
from data_visualizer.profiler import AnalysisReport
print("Pydata-visualizer is installed successfully!")
```

## 2. Basic Usage

### Step 1: Import the library

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport
```

### Step 2: Load your data

```python
# Load data from a CSV file
df = pd.read_csv("your_dataset.csv")

# Or from any other source supported by pandas
# df = pd.read_excel("your_data.xlsx")
# df = pd.read_sql_query("SELECT * FROM your_table", connection)
```

### Step 3: Create an analysis report

```python
# Initialize the report
report = AnalysisReport(df)
```

### Step 4: Generate the HTML report

```python
# Create HTML report
report.to_html("output_report.html")
```

### Step 5: Open the HTML report

Open the generated HTML file in your web browser to view the complete data profile.

## 3. Understanding the Report

The HTML report contains several sections:

### Overview Section

- **Dataset Overview**: Shows basic dataset information
  - Number of rows
  - Number of columns
  - Number of duplicate rows with percentage
  - Duplicate row indices (list of row positions)
  - Duplicate samples (first 5 duplicate row groups shown)
  - Missing values count and percentage (across entire dataset)
  - Dataset-level alerts (e.g., high duplicate rate if exceeds threshold)

### Variables Section

For each column in your dataset:

- **Data type**: Detected data type (pandas dtype)
- **Missing values**: Count and percentage
- **Type-specific statistics**:
  - For numeric: min, max, mean, median, std, quartiles (25%, 50%, 75%), skewness, kurtosis, outlier detection (count, percentage, and indices)
  - For categorical: unique values count, most frequent value, cardinality (High if >50 unique values, Low otherwise), top N value counts (configurable via top_n_values setting)
  - For string/text: unique values count, most frequent value, cardinality (High/Low), top N value counts, word frequency analysis (when text_analysis is enabled)
  - For boolean: value counts and proportions
- **Visualizations**: 
  - Distribution histograms with KDE for numeric data, with outliers highlighted in red (when outliers are detected)
  - Bar charts for categorical data showing top 10 most frequent values
  - Word clouds for text data (when text_analysis is enabled), plus bar charts for value distribution
  - For Plotly mode: interactive charts with zoom, pan, and hover tooltips
  - For Seaborn mode: static, publication-ready images
- **Alerts**: Warnings about potential data issues
  - Missing values alert when >20% of data is missing
  - Outliers alert showing count and percentage
  - Skewness alert when absolute skewness exceeds configured threshold

### Sample Data

- Shows the first 10 rows (head) of your dataset in HTML table format
- Shows the last 10 rows (tail) of your dataset in HTML table format

### Correlations

- **Pearson correlation**: For linear relationships between numerical variables (range: -1 to +1)
- **Spearman correlation**: For monotonic relationships between numerical variables (range: -1 to +1)
- **Cramér's V**: For relationships between categorical variables (range: 0 to 1)
- **Heatmaps**: Visual representation of all correlation matrices (when include_correlations_plots is True)
- **JSON data**: Raw correlation matrices in JSON format (when include_correlations_json is True)

## 4. Advanced Configuration

You can customize the analysis with the `Settings` class:

```python
from data_visualizer.profiler import AnalysisReport, Settings

# Create custom settings
settings = Settings(
    minimal=False,                      # Full analysis with all features
    top_n_values=5,                     # Show top 5 values in categorical columns
    skewness_threshold=2.0,             # Alert threshold for skewness
    outlier_method='iqr',               # Outlier detection method: 'iqr' or 'zscore'
    outlier_threshold=1.5,              # IQR multiplier for outlier detection
    duplicate_threshold=5.0,            # Alert if duplicates exceed 5% of dataset
    text_analysis=True,                 # Enable word frequency and word cloud for text
    use_plotly=False,                   # Use static Seaborn/Matplotlib plots
    include_plots=True,                 # Include visualizations
    include_correlations=True,          # Include correlation analysis
    include_correlations_plots=True,    # Include correlation heatmaps
    include_correlations_json=False,    # Don't include raw correlation JSON
    include_alerts=True,                # Include data quality alerts
    include_sample_data=True,           # Include head/tail samples
    include_overview=True               # Include overview statistics
)

# Apply settings to report
report = AnalysisReport(df, settings=settings)

# Generate the report
report.to_html("custom_report.html")
```

### Settings Options

- **minimal** (bool): If True, performs minimal analysis (faster, skips visualizations and type-specific analysis). Default: False
- **top_n_values** (int): Number of top values to show for categorical variables (must be >= 1). Default: 10
- **skewness_threshold** (float): Threshold for flagging skewed distributions (must be >= 0.0). Default: 1.0
- **outlier_method** (str): Method for outlier detection - 'iqr' (Interquartile Range) or 'zscore'. Default: 'iqr'
- **outlier_threshold** (float): IQR multiplier for outlier detection (must be >= 0.0). Default: 1.5 (use 3.0 for extreme outliers only)
- **duplicate_threshold** (float): Percentage of duplicate rows to trigger an alert (must be >= 0.0). Default: 5.0
- **text_analysis** (bool): Enable word frequency analysis and word cloud generation for text columns. Default: True
- **use_plotly** (bool): Use Plotly for interactive visualizations instead of Seaborn/Matplotlib static plots. Default: False
- **include_plots** (bool): Include visualizations/plots in the analysis. Default: True
- **include_correlations** (bool): Include correlation analysis. Default: True
- **include_correlations_plots** (bool): Include correlation heatmaps. Default: True
- **include_correlations_json** (bool): Include correlation data in JSON format. Default: False
- **include_alerts** (bool): Include data quality alerts (column and dataset-level). Default: True
- **include_sample_data** (bool): Include head/tail data samples (first and last 10 rows). Default: True
- **include_overview** (bool): Include dataset overview statistics. Default: True

## 5. Working with Large Datasets

For large datasets, consider these approaches:

### Use minimal analysis

```python
settings = Settings(
    minimal=True,             # Skip type-specific analysis and visualizations
    include_plots=False       # Also disable plots for fastest processing
)
report = AnalysisReport(large_df, settings=settings)
```

### Sample your data

```python
# Sample 10,000 rows randomly
sampled_df = large_df.sample(10000, random_state=42)
report = AnalysisReport(sampled_df)
```

### Analyze specific columns only

```python
# Select only specific columns for analysis
subset_df = large_df[['important_column_1', 'important_column_2', 'important_column_3']]
report = AnalysisReport(subset_df)
```

## 6. Common Use Cases

### Exploratory Data Analysis (EDA)

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load your dataset
df = pd.read_csv("new_dataset.csv")

# Generate comprehensive EDA report
report = AnalysisReport(df)
report.to_html("eda_report.html")
```

### Data Quality Assessment

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport, Settings

# Load your dataset
df = pd.read_csv("dataset_to_check.csv")

# Set stricter thresholds for data quality
settings = Settings(
    skewness_threshold=1.5,             # Lower threshold for skewness
    duplicate_threshold=3.0,            # Lower threshold for duplicates
    outlier_threshold=1.5,              # Standard IQR multiplier
    include_alerts=True                 # Ensure alerts are included
)

# Generate data quality report
report = AnalysisReport(df, settings=settings)
report.to_html("quality_report.html")
```

### Correlation Discovery

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport, Settings

# Load your dataset
df = pd.read_csv("features.csv")

# Enable correlation JSON output to access correlation data programmatically
settings = Settings(include_correlations_json=True)

# Generate report with focus on correlations
report = AnalysisReport(df, settings=settings)
results = report.analyse()

# Access correlation matrices programmatically
pearson_corr = results['Correlations_JSON']['pearson']
spearman_corr = results['Correlations_JSON']['spearman']

# Find strongly correlated features (absolute correlation > 0.7)
import numpy as np
strong_correlations = [(col1, col2) for col1 in pearson_corr 
                       for col2 in pearson_corr if col1 != col2 
                       and abs(pearson_corr[col1][col2]) > 0.7]

print("Strongly correlated features:", strong_correlations)

# Generate complete report (will include correlation heatmaps)
report.to_html("correlations_report.html")
```

## 7. Customization Options

### Accessing Analysis Results Programmatically

You can access and manipulate the analysis results directly:

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load your dataset
df = pd.read_csv("your_data.csv")

# Run analysis
report = AnalysisReport(df)
results = report.analyse()

# Access specific components
overview = results['overview']
column_stats = results['variables']

# Print summary information
print(f"Dataset has {overview['num_Row']} rows and {overview['num_Columns']} columns")
print(f"Missing values: {overview['missing_percentage']:.2f}%")

# Check specific column statistics
if 'age' in column_stats:
    age_stats = column_stats['age']
    print(f"Age statistics: Min={age_stats.get('min')}, Max={age_stats.get('max')}, Mean={age_stats.get('mean')}")
```

### Customizing Report Output

You can generate the HTML report to a specific location:

```python
# Generate report to specific path
report.to_html("/path/to/reports/analysis_report.html")
```

### Integrating with Other Tools

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport
import webbrowser
import os

# Load your dataset
df = pd.read_csv("your_data.csv")

# Create and generate report
report_path = "analysis_report.html"
report = AnalysisReport(df)
report.to_html(report_path)

# Automatically open the report in the default browser
webbrowser.open('file://' + os.path.abspath(report_path))
```

## Conclusion

This guide covered the essential aspects of using Pydata-visualizer for data analysis and profiling. For more detailed information, refer to the [full documentation](https://github.com/Adi-Deshmukh/Pydata-visualizer) or explore the source code.
