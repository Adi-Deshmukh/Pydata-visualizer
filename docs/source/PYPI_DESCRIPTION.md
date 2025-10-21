# Pydata-visualizer

A powerful and intuitive Python library for exploratory data analysis and data profiling.

## Overview

Pydata-visualizer automatically analyzes your dataset, generates interactive visualizations, and provides detailed statistical insights with minimal code. It's designed to streamline the initial exploration phase of your data science workflow.

## Features

- **Comprehensive Data Profiling**: Analyze numerical, categorical, boolean, and string data types with detailed statistics
- **Automated Data Quality Checks**: Detect missing values, outliers (IQR/Z-score methods), skewed distributions, duplicate rows (with indices and samples), and more
- **Interactive Visualizations**: Generate distribution plots, correlation heatmaps, word clouds, and statistical charts using Plotly or Seaborn
- **Dual Rendering Modes**: Choose between interactive Plotly charts or static Seaborn/Matplotlib visualizations
- **Text Analysis**: Automatic word frequency analysis and word cloud generation for text columns
- **Rich HTML Reports**: Export analysis to visually appealing and shareable HTML reports with interactive or static charts
- **Performance Optimized**: Fast analysis even on large datasets with minimal mode and modular settings
- **Correlation Analysis**: Calculate Pearson, Spearman, and Cramér's V correlations between variables
- **Flexible Configuration**: Customize analysis thresholds and options via the comprehensive Settings class with 15+ configurable parameters
- **Modular Analysis**: Toggle individual components (plots, correlations, alerts, sample data, overview) on/off for customized reports

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
    minimal=False,                      # Set to True for faster, minimal analysis
    top_n_values=5,                     # Show top 5 values in categorical columns
    skewness_threshold=2.0,             # Tolerance for skewness alerts
    outlier_method='iqr',               # Outlier detection method: 'iqr' or 'zscore'
    outlier_threshold=1.5,              # IQR multiplier for outlier detection
    duplicate_threshold=5.0,            # Percentage threshold for duplicate alerts
    text_analysis=True,                 # Enable word frequency analysis for text columns
    use_plotly=True,                    # Use Plotly for interactive visualizations (default: False for Seaborn)
    include_plots=True,                 # Include visualizations/plots
    include_correlations=True,          # Include correlation analysis
    include_correlations_plots=True,    # Include correlation heatmaps
    include_correlations_json=False,    # Include correlation data in JSON format
    include_alerts=True,                # Include data quality alerts
    include_sample_data=True,           # Include head/tail samples
    include_overview=True               # Include dataset overview statistics
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
- wordcloud
- plotly

## Links

- Homepage: [https://github.com/Adi-Deshmukh/Pydata-visualizer](https://github.com/Adi-Deshmukh/Pydata-visualizer)
- Documentation: [https://github.com/Adi-Deshmukh/Pydata-visualizer/blob/main/DOCUMENTATION.md](https://github.com/Adi-Deshmukh/Pydata-visualizer/blob/main/DOCUMENTATION.md)
- Bug Reports: [https://github.com/Adi-Deshmukh/Pydata-visualizer/issues](https://github.com/Adi-Deshmukh/Pydata-visualizer/issues)

## License

MIT
