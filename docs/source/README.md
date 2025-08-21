# Pydata-visualizer

[![PyPI version](https://img.shields.io/pypi/v/pydata-visualizer.svg)](https://pypi.org/project/pydata-visualizer/)
[![Python versions](https://img.shields.io/pypi/pyversions/pydata-visualizer.svg)](https://pypi.org/project/pydata-visualizer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful and intuitive Python library for exploratory data analysis and data profiling. Pydata-visualizer automatically analyzes your dataset, generates interactive visualizations, and provides detailed statistical insights with minimal code.

## Features

-  **Comprehensive Data Profiling**: Analyze numerical, categorical, boolean, and string data types
-  **Automated Data Quality Checks**: Detect missing values, outliers, skewed distributions, and more
-  **Interactive Visualizations**: Generate distribution plots, correlations heatmaps, and statistical charts
-  **Rich HTML Reports**: Export analysis to visually appealing and shareable HTML reports
-  **Performance Optimized**: Fast analysis even on large datasets
-  **Correlation Analysis**: Calculate Pearson, Spearman, and Cramér's V correlations between variables

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
    minimal=False,          # Set to True for faster, minimal analysis
    top_n_values=5,         # Show top 5 values in categorical columns
    skewness_threshold=2.0  # Tolerance for skewness alerts
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

- **Overview**: Dataset dimensions, missing values, duplicate rows
- **Variable Analysis**: Detailed per-column statistics and visualizations
- **Sample Data**: Head and tail samples of the dataset
- **Correlations**: Correlation matrices and heatmaps

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
        Whether to perform minimal analysis
    top_n_values : int, default=10
        Number of top values to show for categorical columns
    skewness_threshold : float, default=1.0
        Threshold for skewness alerts
    """
```

## Type Analyzers

The library automatically detects and applies the appropriate analysis for different data types:

- **Numeric**: Statistical measures, distribution plots, skewness, kurtosis
- **Categorical/String**: Value counts, cardinality, frequency distributions
- **Boolean**: Value counts and proportions
- **Generic**: Basic analysis for unrecognized types

## Correlation Analysis

Three correlation methods are calculated when possible:

- **Pearson**: Linear correlation between numerical variables
- **Spearman**: Rank correlation capturing monotonic relationships
- **Cramér's V**: Measure of association between categorical variables

## Data Quality Alerts

The library automatically detects potential issues in your data:

- **High Missing Values**: Columns with significant missing data
- **Skewness**: Highly skewed distributions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

Created by Aditya Deshmukh (adideshmukh2005@gmail.com)

GitHub: [https://github.com/Adi-Deshmukh/Pydata-visualizer](https://github.com/Adi-Deshmukh/Pydata-visualizer)
