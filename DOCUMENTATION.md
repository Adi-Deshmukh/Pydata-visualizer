# Pydata-visualizer Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Basic Usage](#basic-usage)
4. [Core Components](#core-components)
5. [Settings Configuration](#settings-configuration)
6. [Analysis Methods](#analysis-methods)
7. [Visualization Features](#visualization-features)
8. [Correlation Analysis](#correlation-analysis)
9. [Data Quality Alerts](#data-quality-alerts)
10. [HTML Report Generation](#html-report-generation)
11. [API Reference](#api-reference)
12. [Examples](#examples)
13. [Extending the Library](#extending-the-library)
14. [Troubleshooting](#troubleshooting)

## Introduction

Pydata-visualizer is a Python library designed for exploratory data analysis and data profiling. It automatically analyzes datasets, providing detailed statistical insights, visualizations, and interactive HTML reports with minimal code requirements.

The library aims to streamline the initial data exploration phase of the data science workflow, helping users quickly understand their data's structure, distribution, and quality.

## Installation

### Requirements

- Python 3.8 or higher
- Core dependencies: pandas, numpy, matplotlib, seaborn, scipy, jinja2

### Install from PyPI

```bash
pip install pydata-visualizer
```

### Install from Source

```bash
git clone https://github.com/Adi-Deshmukh/Data_Profiler.git
cd Data_Profiler
pip install -e .
```

## Basic Usage

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load your dataset
df = pd.read_csv("your_dataset.csv")

# Create and generate a report
report = AnalysisReport(df)
report.to_html("report.html")
```

This simple code will:
1. Analyze all columns in your dataset
2. Generate appropriate visualizations for each column
3. Calculate correlations between columns
4. Create an interactive HTML report

## Core Components

### Main Modules

- **profiler.py**: Core analysis functionality, including `AnalysisReport` and `Settings` classes
- **visualizer.py**: Creates visualizations for different data types
- **type_analyzers.py**: Type-specific analysis functions
- **correlations.py**: Correlation calculation between variables
- **alerts.py**: Data quality alert generation
- **report.py**: HTML report generation

### Data Flow

1. **Data Input**: User provides pandas DataFrame
2. **Type Detection**: Library detects column data types
3. **Analysis**: Type-specific analysis is performed
4. **Visualization**: Appropriate plots are generated
5. **Correlation**: Relationships between variables are calculated
6. **Report Generation**: Results are compiled into HTML report

## Settings Configuration

The `Settings` class allows customization of the analysis process:

```python
from data_visualizer.profiler import Settings, AnalysisReport

# Custom settings
settings = Settings(
    minimal=False,           # Full analysis (True for faster, minimal analysis)
    top_n_values=5,          # Show top 5 values in categorical columns
    skewness_threshold=2.0   # Alert threshold for skewness
)

# Create report with custom settings
report = AnalysisReport(df, settings=settings)
report.to_html("custom_report.html")
```

### Available Settings

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| minimal | bool | False | If True, performs basic analysis only |
| top_n_values | int | 10 | Number of top values to show in categorical analysis |
| skewness_threshold | float | 1.0 | Threshold for skewness alerts |

## Analysis Methods

### Overview Statistics

- Row count
- Column count
- Duplicate rows count
- Missing value count and percentage

### Numeric Column Analysis

- Standard statistics (min, max, mean, median, etc.)
- Skewness and kurtosis
- Distribution histograms with KDE

### Categorical Column Analysis

- Unique value count
- Most frequent value
- Cardinality assessment
- Top N value counts
- Bar charts for frequency distribution

### Boolean Column Analysis

- Value counts and proportions
- Distribution visualization

## Visualization Features

The library automatically generates appropriate visualizations based on data type:

- **Numeric columns**: Histograms with kernel density estimation
- **Categorical columns**: Bar charts for top values
- **Correlation matrices**: Heatmap visualizations

Visualizations are embedded directly in the HTML report as base64-encoded images.

## Correlation Analysis

Three correlation methods are calculated:

### Pearson Correlation

- Measures linear relationships between numerical variables
- Values range from -1 (perfect negative) to +1 (perfect positive)
- Visualized as a heatmap

### Spearman Correlation

- Measures monotonic relationships between numerical variables
- Less sensitive to outliers than Pearson
- Visualized as a heatmap

### Cramér's V

- Measures association between categorical variables
- Values range from 0 (no association) to 1 (perfect association)
- Visualized as a heatmap

## Data Quality Alerts

The library automatically detects potential issues in your data:

- **Missing Values**: Warns when columns have significant missing data (>20%)
- **Skewness**: Flags highly skewed distributions based on threshold

Alerts are displayed prominently in the HTML report with warning icons and explanatory messages.

## HTML Report Generation

The HTML report contains:

1. **Overview panel**: Dataset dimensions and summary
2. **Variables panel**: Detailed per-column analysis
   - Type information
   - Statistical measures
   - Visualizations
   - Data quality alerts
3. **Sample Data**: Head and tail sample rows
4. **Correlations**: Correlation matrices and heatmaps

The report is fully interactive with Bootstrap styling, allowing for:
- Collapsible sections
- Sortable tables
- Interactive visualizations

## API Reference

### AnalysisReport

```python
class AnalysisReport:
    """
    Main class for dataset analysis.
    """
    
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
            A dictionary containing all analysis results with keys:
            - 'overview': Dataset statistics
            - 'variables': Per-column analysis
            - 'Sample_data': DataFrame head and tail
            - 'Correlations_Plots': Visualization of correlations
            - 'Correlations_JSON': Raw correlation data
        """
        
    def to_html(self, filename="report.html"):
        """
        Generate an HTML report from the analysis.
        
        Parameters:
        -----------
        filename : str, optional
            Path to save the HTML report (default: "report.html")
        """
        
    def _analyze_column(self, column_data, column_name):
        """
        Analyze a single column of data.
        
        Parameters:
        -----------
        column_data : pandas.Series
            The column data to analyze
        column_name : str
            The name of the column
            
        Returns:
        --------
        dict
            Dictionary of analysis results for the column
        """
        
    def _data_sample(self):
        """
        Create HTML samples of the dataset head and tail.
        
        Returns:
        --------
        dict
            Dictionary with HTML representations of head and tail
        """
```

### Settings

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

## Examples

### Basic Analysis

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load dataset
df = pd.read_csv("customer_data.csv")

# Create and generate report
report = AnalysisReport(df)
report.to_html("customer_analysis.html")
```

### Using Analysis Results Programmatically

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport, Settings

# Load dataset
df = pd.read_csv("financial_data.csv")

# Configure settings for financial data
settings = Settings(skewness_threshold=3.0, top_n_values=3)

# Create report
report = AnalysisReport(df, settings=settings)

# Run analysis and get results dictionary
results = report.analyse()

# Access specific insights
overview = results['overview']
missing_percentage = overview['missing_percentage']
print(f"Dataset has {missing_percentage:.2f}% missing values")

# Check skewness of a specific column
column_stats = results['variables']['income']
if 'skewness' in column_stats:
    print(f"Income skewness: {column_stats['skewness']:.2f}")

# Generate report
report.to_html("financial_analysis.html")
```

## Extending the Library

### Registering Custom Type Analyzers

You can extend the library by registering custom analyzers for specific data types:

```python
from data_visualizer.type_registry import register_analyzer
from visions.types import DateTime

@register_analyzer(DateTime)
def _analyze_datetime(report_object, column_data):
    """Custom analyzer for datetime columns"""
    datetime_stats = {
        'min_date': column_data.min(),
        'max_date': column_data.max(),
        'range_days': (column_data.max() - column_data.min()).days,
        'weekday_counts': column_data.dt.day_name().value_counts().to_dict()
    }
    return datetime_stats
```

## Troubleshooting

### Common Issues

#### Missing Dependencies

If you encounter import errors, ensure all dependencies are installed:

```bash
pip install "pydata-visualizer[complete]"
```

#### Memory Issues with Large Datasets

For large datasets, use the minimal setting:

```python
from data_visualizer.profiler import AnalysisReport, Settings

# Memory-efficient settings
settings = Settings(minimal=True)
report = AnalysisReport(large_df, settings=settings)
```

#### Visualization Errors

If visualizations fail to generate, check matplotlib backend:

```python
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
```

#### Character Encoding Issues

For datasets with special characters, ensure proper encoding:

```python
df = pd.read_csv("international_data.csv", encoding="utf-8")
```
