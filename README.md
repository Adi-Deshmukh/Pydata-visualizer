# Pydata-visualizer

[![PyPI version](https://img.shields.io/pypi/v/pydata-visualizer.svg)](https://pypi.org/project/pydata-visualizer/)
[![Python versions](https://img.shields.io/pypi/pyversions/pydata-visualizer.svg)](https://pypi.org/project/pydata-visualizer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful and intuitive Python library for exploratory data analysis and data profiling. Pydata-visualizer automatically analyzes your dataset, generates interactive visualizations, and provides detailed statistical insights with minimal code.

## Features

- **Comprehensive Data Profiling**: Analyze numerical, categorical, boolean, and string data types with detailed statistics
- **Automated Data Quality Checks**: Detect missing values, outliers (IQR/Z-score methods), skewed distributions, duplicate rows, and more
- **Interactive Visualizations**: Generate distribution plots, correlation heatmaps, word clouds, and statistical charts using Plotly or Seaborn
- **Dual Rendering Modes**: Choose between interactive Plotly charts or static Seaborn/Matplotlib visualizations
- **Text Analysis**: Automatic word frequency analysis and word cloud generation for text columns
- **Rich HTML Reports**: Export analysis to visually appealing and shareable HTML reports with interactive or static charts
- **Performance Optimized**: Fast analysis even on large datasets with minimal mode and modular settings
- **Correlation Analysis**: Calculate Pearson, Spearman, and Cramér's V correlations between variables
- **Flexible Configuration**: Customize analysis thresholds and options via the comprehensive Settings class
- **Modular Analysis**: Toggle individual components (plots, correlations, alerts, sample data, overview) on/off

## Installation

```bash
pip install pydata-visualizer
```

## Quick Start

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport, Settings

# Load your dataset
df = pd.read_csv("your_dataset.csv")

# Create a report with default settings
report = AnalysisReport(df)
report.to_html("report.html")
```

## Advanced Usage

### Customizing Analysis Settings

```python
from data_visualizer.profiler import AnalysisReport, Settings

# Configure analysis settings
report_settings = Settings(
    minimal=False,                      # Set to True for faster, minimal analysis
    top_n_values=5,                     # Show top 5 values in categorical columns
    skewness_threshold=2.0,             # Tolerance for skewness alerts
    outlier_method='iqr',               # Outlier detection method: 'iqr' or 'zscore'
    outlier_threshold=1.5,              # IQR multiplier for outlier detection
    duplicate_threshold=5.0,            # Percentage threshold for duplicate alerts
    text_analysis=True,                 # Enable word frequency analysis for text columns
    use_plotly=True,                    # Use Plotly for interactive visualizations (default: False for Seaborn)
    include_plots=True,                 # Include visualizations/plots in the analysis
    include_correlations=True,          # Include correlation analysis
    include_correlations_plots=True,    # Include correlation heatmaps
    include_correlations_json=False,    # Include correlation data in JSON format
    include_alerts=True,                # Include data quality alerts
    include_sample_data=True,           # Include head/tail samples
    include_overview=True               # Include dataset overview statistics
)

# Create report with custom settings
report = AnalysisReport(df, settings=report_settings)

# Perform analysis and get results dictionary
results = report.analyse()

# Generate HTML report
report.to_html("custom_report.html")
```

### Report Structure

The generated report includes:

- **Overview**: Dataset dimensions, missing values, duplicate rows (count, percentage, indices, and samples of duplicate data)
- **Variable Analysis**: Detailed per-column statistics and visualizations including:
  - Distribution plots for numeric data with outlier highlighting (outliers shown in red)
  - Bar charts for categorical data
  - Word clouds and bar charts for text data (when text_analysis is enabled)
  - Outlier detection using IQR or Z-score methods with outlier counts and percentages
  - Skewness and kurtosis for numeric columns
  - Cardinality assessment (High/Low) for categorical and text columns
- **Sample Data**: Head and tail samples of the dataset (first and last 10 rows)
- **Correlations**: Correlation matrices and heatmaps for:
  - Pearson correlation (linear relationships between numerical variables)
  - Spearman correlation (monotonic relationships between numerical variables)
  - Cramér's V (associations between categorical variables)
- **Data Quality Alerts**: Automated detection of data quality issues:
  - High Missing Values (>20% threshold)
  - Skewness (configurable threshold, default 1.0)
  - Outliers (detected via IQR or Z-score methods)
  - High Duplicates (configurable percentage threshold, default 5.0%)

## API Reference

### `AnalysisReport` Class

```python
class AnalysisReport:
    def __init__(self, data, settings=None):
        """
        Initialize the analysis report object.
        
        Parameters:
        -----------
        data : pandas.DataFrame
            The dataset to analyze
        settings : Settings, optional
            Configuration settings for the analysis
        """
        
    def analyse(self):
        """
        Perform the data analysis.
        
        Returns:
        --------
        dict
            A dictionary containing all analysis results
        """
        
    def to_html(self, filename="report.html"):
        """
        Generate an HTML report from the analysis.
        
        Parameters:
        -----------
        filename : str, optional
            Path to save the HTML report (default: "report.html")
        """
```

### `Settings` Class

```python
class Settings(pydantic.BaseModel):
    """
    Settings for the analysis report.
    
    Attributes:
    -----------
    minimal : bool, default=False
        Whether to perform minimal analysis (skips type-specific analysis and visualizations)
    
    top_n_values : int, default=10
        Number of top values to show for categorical columns (must be >= 1)
    
    skewness_threshold : float, default=1.0
        Threshold for skewness alerts (must be >= 0.0)
    
    outlier_method : str, default='iqr'
        Outlier detection method: 'iqr' (Interquartile Range) or 'zscore'
    
    outlier_threshold : float, default=1.5
        IQR multiplier for outlier detection (must be >= 0.0)
        Standard: 1.5 for moderate outliers, 3.0 for extreme outliers
    
    duplicate_threshold : float, default=5.0
        Percentage of duplicate rows to trigger an alert (must be >= 0.0)
    
    text_analysis : bool, default=True
        Enable word frequency analysis and word cloud generation for text columns
    
    use_plotly : bool, default=False
        Use Plotly for interactive visualizations instead of Seaborn/Matplotlib static plots
    
    include_plots : bool, default=True
        Include visualizations/plots in the analysis
    
    include_correlations : bool, default=True
        Include correlation analysis
    
    include_correlations_plots : bool, default=True
        Include correlation heatmaps
    
    include_correlations_json : bool, default=False
        Include correlation data in JSON format
    
    include_alerts : bool, default=True
        Include data quality alerts (column and dataset-level)
    
    include_sample_data : bool, default=True
        Include head/tail data samples
    
    include_overview : bool, default=True
        Include dataset overview statistics
    """
```

## Type Analyzers

The library automatically detects and applies the appropriate analysis for different data types:

- **Numeric (Integer/Float)**: Statistical measures (mean, std, min, max, quartiles), distribution plots with KDE, skewness, kurtosis, outlier detection (IQR/Z-score methods), outlier counts and percentages, outlier highlighting in visualizations
- **Categorical/Object**: Value counts, cardinality analysis (High/Low based on 50 unique values threshold), frequency distributions, top N values (configurable), bar charts
- **String**: Unique value counts, cardinality analysis (High/Low), top N values (configurable), word frequency analysis (when text_analysis is enabled), word cloud generation (Plotly scatter or WordCloud library), bar charts for value distribution
- **Boolean**: Value counts, proportions, and frequency distribution visualizations
- **Generic**: Basic analysis (unique value count) for unrecognized types

## Correlation Analysis

Three correlation methods are calculated when applicable:

- **Pearson**: Linear correlation between numerical variables (range: -1 to 1)
- **Spearman**: Rank correlation capturing monotonic relationships (range: -1 to 1)
- **Cramér's V**: Measure of association between categorical variables (range: 0 to 1)

## Data Quality Alerts

The library automatically detects potential issues in your data:

- **High Missing Values**: Columns with more than 20% missing data
- **Skewness**: Distributions exceeding the configured skewness threshold
- **Outliers**: Data points detected using IQR or Z-score methods
- **High Duplicates**: Duplicate rows exceeding the configured threshold percentage

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

Created by Aditya Deshmukh (adideshmukh2005@gmail.com)

GitHub: [https://github.com/Adi-Deshmukh/Pydata-visualizer](https://github.com/Adi-Deshmukh/Pydata-visualizer)
