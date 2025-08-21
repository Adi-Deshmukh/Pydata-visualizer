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
  - Number of duplicate rows
  - Missing values count and percentage

### Variables Section

For each column in your dataset:

- **Data type**: Detected data type
- **Missing values**: Count and percentage
- **Type-specific statistics**:
  - For numeric: min, max, mean, median, std, quartiles, skewness, kurtosis
  - For categorical: unique values, most frequent values, cardinality
  - For boolean: value counts and proportions
- **Visualizations**: Distribution plots or bar charts
- **Alerts**: Warnings about potential data issues

### Sample Data

- Shows the first and last 10 rows of your dataset

### Correlations

- **Pearson correlation**: For linear relationships between numerical variables
- **Spearman correlation**: For monotonic relationships
- **Cramér's V**: For relationships between categorical variables
- **Heatmaps**: Visual representation of all correlation matrices

## 4. Advanced Configuration

You can customize the analysis with the `Settings` class:

```python
from data_visualizer.profiler import AnalysisReport, Settings

# Create custom settings
settings = Settings(
    minimal=False,           # Full analysis
    top_n_values=5,          # Show top 5 values in categorical columns
    skewness_threshold=2.0   # Alert threshold for skewness
)

# Apply settings to report
report = AnalysisReport(df, settings=settings)

# Generate the report
report.to_html("custom_report.html")
```

### Settings Options

- **minimal** (bool): If True, performs minimal analysis (faster)
- **top_n_values** (int): Number of top values to show for categorical variables
- **skewness_threshold** (float): Threshold for flagging skewed distributions

## 5. Working with Large Datasets

For large datasets, consider these approaches:

### Use minimal analysis

```python
settings = Settings(minimal=True)
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
settings = Settings(skewness_threshold=1.5)

# Generate data quality report
report = AnalysisReport(df, settings=settings)
report.to_html("quality_report.html")
```

### Correlation Discovery

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load your dataset
df = pd.read_csv("features.csv")

# Generate report with focus on correlations
report = AnalysisReport(df)
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

# Generate complete report
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
