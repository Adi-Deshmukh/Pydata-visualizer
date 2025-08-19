# Pydata-visualizer Documentation

Welcome to the official documentation for Pydata-visualizer, a powerful Python library for exploratory data analysis and data profiling.

## Overview

Pydata-visualizer is designed to help data scientists and analysts quickly explore, understand, and visualize their datasets. With minimal code, you can generate comprehensive reports and gain insights into your data's structure, distribution, and quality.

### Key Features

-  **Comprehensive Data Profiling**: Analyze numerical, categorical, boolean, and string data types
-  **Automated Data Quality Checks**: Detect missing values, outliers, skewed distributions, and more
-  **Interactive Visualizations**: Generate distribution plots, correlations heatmaps, and statistical charts
-  **Rich HTML Reports**: Export analysis to visually appealing and shareable HTML reports
-  **Performance Optimized**: Fast analysis even on large datasets
-  **Correlation Analysis**: Calculate Pearson, Spearman, and Cramér's V correlations between variables

### Quick Example

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load your dataset
df = pd.read_csv("your_dataset.csv")

# Create a report with default settings
report = AnalysisReport(df)
report.to_html("report.html")
```

## Indices and Tables

* {ref}`genindex`
* {ref}`modindex`
* {ref}`search`
