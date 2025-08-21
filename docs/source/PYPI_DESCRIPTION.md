# Pydata-visualizer

A powerful and intuitive Python library for exploratory data analysis and data profiling.

## Overview

Pydata-visualizer automatically analyzes your dataset, generates interactive visualizations, and provides detailed statistical insights with minimal code. It's designed to streamline the initial exploration phase of your data science workflow.

## Features

- **Comprehensive Data Profiling**: Analyze numerical, categorical, boolean, and string data types with detailed statistics
- **Automated Data Quality Checks**: Detect missing values, outliers, skewed distributions, and more
- **Interactive Visualizations**: Generate distribution plots, correlations heatmaps, and statistical charts
- **Rich HTML Reports**: Export analysis to visually appealing and shareable HTML reports
- **Performance Optimized**: Fast analysis even on large datasets
- **Correlation Analysis**: Calculate Pearson, Spearman, and Cramér's V correlations between variables

## Installation

```bash
pip install pydata-visualizer
```

## Quick Start

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load your dataset
df = pd.read_csv("your_dataset.csv")

# Create a report with default settings
report = AnalysisReport(df)
report.to_html("report.html")
```

## Advanced Usage

```python
from data_visualizer.profiler import AnalysisReport, Settings

# Configure analysis settings
settings = Settings(
    minimal=False,          # Set to True for faster, minimal analysis
    top_n_values=5,         # Show top 5 values in categorical columns
    skewness_threshold=2.0  # Tolerance for skewness alerts
)

# Create report with custom settings
report = AnalysisReport(df, settings=settings)
report.to_html("custom_report.html")
```

## Requirements

- Python 3.8+
- pandas
- matplotlib
- seaborn
- numpy
- scipy
- jinja2
- visions
- pydantic
- colorama
- tqdm
- imagehash

## Links

- Homepage: [https://github.com/Adi-Deshmukh/Pydata-visualizer](https://github.com/Adi-Deshmukh/Pydata-visualizer)
- Documentation: [https://github.com/Adi-Deshmukh/Pydata-visualizer/blob/main/DOCUMENTATION.md](https://github.com/Adi-Deshmukh/Pydata-visualizer/blob/main/DOCUMENTATION.md)
- Bug Reports: [https://github.com/Adi-Deshmukh/Pydata-visualizer/issues](https://github.com/Adi-Deshmukh/Pydata-visualizer/issues)

## License

MIT
