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
- Core dependencies: pandas, numpy, matplotlib, seaborn, scipy, jinja2, plotly, wordcloud, visions, pydantic, colorama, tqdm

### Install from PyPI

```bash
pip install pydata-visualizer
```

### Install from Source

```bash
git clone https://github.com/Adi-Deshmukh/Pydata-visualizer.git
cd Pydata-visualizer
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

### Core Modules

- **profiler.py**: Core analysis functionality, including `AnalysisReport` class and the main analysis logic. Entry point for all analysis operations.
- **settings.py**: Configuration settings via the `Settings` Pydantic model with validation
- **visualizer.py**: Creates visualizations for different data types using Plotly or Seaborn/Matplotlib
- **type_analyzers.py**: Type-specific analysis functions for numeric, categorical, string, boolean, and generic data types
- **type_registry.py**: Decorator-based registry system for registering custom type analyzers
- **correlations.py**: Correlation calculation (Pearson, Spearman, Cramér's V) and heatmap generation
- **alerts.py**: Data quality alert generation for column-level and dataset-level issues
- **report.py**: HTML report generation using Jinja2 templates

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
    minimal=False,                      # Full analysis (True for faster, minimal analysis)
    top_n_values=5,                     # Show top 5 values in categorical columns
    skewness_threshold=2.0,             # Alert threshold for skewness
    outlier_method='iqr',               # Outlier detection method: 'iqr' or 'zscore'
    outlier_threshold=1.5,              # IQR multiplier for outlier detection
    duplicate_threshold=5.0,            # Alert if duplicates exceed 5% of dataset
    text_analysis=True,                 # Enable word frequency analysis for text columns
    use_plotly=True,                    # Use Plotly for interactive visualizations
    include_plots=True,                 # Include visualizations/plots
    include_correlations=True,          # Include correlation analysis
    include_correlations_plots=True,    # Include correlation heatmaps
    include_correlations_json=False,    # Don't include raw correlation JSON
    include_alerts=True,                # Include data quality alerts
    include_sample_data=True,           # Include head/tail samples
    include_overview=True               # Include overview statistics
)

# Create report with custom settings
report = AnalysisReport(df, settings=settings)
report.to_html("custom_report.html")
```

### Available Settings

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| minimal | bool | False | If True, performs basic analysis only (skips visualizations) |
| top_n_values | int | 10 | Number of top values to show in categorical analysis (>= 1) |
| skewness_threshold | float | 1.0 | Threshold for skewness alerts (>= 0.0) |
| outlier_method | str | 'iqr' | Outlier detection method: 'iqr' or 'zscore' |
| outlier_threshold | float | 1.5 | IQR multiplier for outlier detection (>= 0.0) |
| duplicate_threshold | float | 5.0 | Percentage of duplicates to trigger alert (>= 0.0) |
| text_analysis | bool | True | Enable word frequency analysis and word clouds for text |
| use_plotly | bool | False | Use Plotly for interactive visualizations instead of Seaborn/Matplotlib |
| include_plots | bool | True | Include visualizations/plots in the analysis |
| include_correlations | bool | True | Include correlation analysis |
| include_correlations_plots | bool | True | Include correlation heatmaps |
| include_correlations_json | bool | False | Include correlation data in JSON format |
| include_alerts | bool | True | Include data quality alerts |
| include_sample_data | bool | True | Include head/tail data samples |
| include_overview | bool | True | Include dataset overview statistics |

## Analysis Methods

### Overview Statistics

- Row count (num_Row)
- Column count (num_Columns)
- Duplicate rows count (duplicated_rows)
- Duplicate percentage (duplicate_percentage)
- Duplicate row indices (duplicate_indices) - list of row positions
- Duplicate samples (duplicate_samples) - first 5 duplicate row groups
- Missing value count (across entire dataset)
- Missing percentage (across entire dataset)
- Dataset-level alerts (when include_alerts is True)

### Numeric Column Analysis

- Standard statistics: min, max, mean, median, std (standard deviation), quartiles (25%, 50%, 75%)
- Skewness (measure of distribution asymmetry)
- Kurtosis (measure of distribution tailedness)
- Outlier detection using IQR (Interquartile Range) or Z-score methods (configurable)
- Outlier count (number of outlier values detected)
- Outlier percentage (percentage of total values that are outliers)
- Outlier indices (list of row positions with outliers, used for visualization highlighting)
- Distribution histograms with KDE (Kernel Density Estimation)
- Outlier highlighting in visualizations (outliers shown in red on histograms)
- Alerts for high skewness and outliers (when include_alerts is True)

### Categorical Column Analysis

- Unique value count (num_unique or unique_values)
- Most frequent value (mode)
- Cardinality assessment: "High" if >50 unique values, "Low" otherwise
- Top N value counts (configurable via top_n_values setting, default 10)
- Bar charts showing frequency distribution of top 10 most frequent values
- Rotated x-axis labels for better readability

### String/Text Column Analysis

- Unique value count (num_unique)
- Most frequent value (mode)
- Cardinality assessment: "High" if >50 unique values, "Low" otherwise
- Top N value counts (configurable via top_n_values setting, default 10)
- Word frequency analysis (when text_analysis is enabled): extracts words, counts frequencies, returns top 10 most common words
- Word cloud generation (when text_analysis and include_plots are enabled):
  - Plotly mode: scatter plot with sized text labels
  - Seaborn mode: WordCloud library with customizable colormap
- Bar charts for value distribution (top 10 most frequent complete values)
- Both word cloud and bar chart can be generated for the same column

### Boolean Column Analysis

- Value counts and proportions
- Distribution visualization

## Visualization Features

The library automatically generates appropriate visualizations based on data type:

- **Numeric columns**: Histograms with kernel density estimation (KDE)
  - Outliers highlighted in red when detected via IQR or Z-score methods
  - Inliers shown in teal/blue (#17a2b8)
  - Legend distinguishing inliers and outliers
  
- **Categorical columns**: Bar charts for top 10 most frequent values
  - Viridis colormap for visual appeal
  - Rotated x-axis labels (45 degrees) for readability
  
- **Text columns**: 
  - Word clouds showing word frequency (when text_analysis is enabled)
    - Plotly: scatter plot with sized text
    - Seaborn: WordCloud library with white background and viridis colormap
  - Bar charts for value distribution (top 10 complete values)
  
- **Correlation matrices**: Heatmap visualizations
  - Coolwarm colormap showing positive (red) and negative (blue) correlations
  - Annotated with correlation values (2 decimal places)
  - Square aspect ratio for better visual balance

**Visualization Formats**:
- **Plotly mode** (when use_plotly=True): Interactive charts with zoom, pan, hover tooltips, responsive design
- **Seaborn/Matplotlib mode** (default): Static, publication-ready PNG images encoded as base64 for HTML embedding

## Correlation Analysis

Three correlation methods are calculated:

### Pearson Correlation

- Measures linear relationships between numerical variables
- Values range from -1 (perfect negative linear correlation) to +1 (perfect positive linear correlation)
- 0 indicates no linear correlation
- Calculated using pandas `.corr(method='pearson')`
- Only applied to numeric columns
- Visualized as a heatmap with coolwarm colormap

### Spearman Correlation

- Measures monotonic relationships between numerical variables (not just linear)
- Less sensitive to outliers than Pearson correlation
- Values range from -1 (perfect negative monotonic correlation) to +1 (perfect positive monotonic correlation)
- Calculated using pandas `.corr(method='spearman')`
- Only applied to numeric columns
- Visualized as a heatmap with coolwarm colormap

### Cramér's V

- Measures association between categorical variables (not correlation, but association strength)
- Values range from 0 (no association) to 1 (perfect association)
- Based on chi-squared test of independence
- Calculated for all pairs of categorical columns using contingency tables
- Formula: V = sqrt(chi² / (n * (min_dim - 1)))
  - chi²: Chi-squared statistic from contingency table
  - n: Total number of observations
  - min_dim: Minimum dimension of the contingency table
- Returns 0.0 if ZeroDivisionError occurs (constant column)
- Result stored in symmetric matrix with diagonal values of 1.0
- Only applied to object/categorical columns
- Visualized as a heatmap with coolwarm colormap

**Correlation Output Options**:
- **Correlations_Plots**: Base64-encoded heatmap images (when include_correlations_plots is True)
- **Correlations_JSON**: Raw correlation matrices as nested dictionaries (when include_correlations_json is True)
- Correlations are only calculated and included when include_correlations is True

## Data Quality Alerts

The library automatically detects potential issues in your data (when include_alerts is True):

### Column-Level Alerts

- **Missing Values**: Warns when columns have significant missing data (>20% threshold, hardcoded)
  - Alert type: "High Missing Values"
  - Shows percentage of missing values
  
- **Skewness**: Flags highly skewed distributions based on configurable threshold
  - Alert type: "skewness"
  - Default threshold: 1.0 (configurable via settings.skewness_threshold)
  - Triggered when |skewness| > threshold
  - Shows actual skewness value
  
- **Outliers**: Alerts when outliers are detected in numeric columns
  - Alert type: "Outliers"
  - Detection method configurable: 'iqr' or 'zscore'
  - Shows outlier count and percentage
  - IQR method: uses configurable multiplier (default 1.5)

### Dataset-Level Alerts

- **High Duplicates**: Warns when duplicate rows exceed a threshold
  - Alert type: "High Duplicates"
  - Default threshold: 5.0% (configurable via settings.duplicate_threshold)
  - Shows actual duplicate percentage

Alerts are displayed prominently in the HTML report with warning icons and explanatory messages.

## HTML Report Generation

The HTML report is generated using Jinja2 templates and contains:

1. **Overview panel**: Dataset dimensions and summary statistics
   - Number of rows and columns
   - Duplicate rows (count, percentage, indices, samples)
   - Missing values (count and percentage across entire dataset)
   - Dataset-level alerts
   
2. **Variables panel**: Detailed per-column analysis
   - Data type information (pandas dtype)
   - Missing value statistics
   - Type-specific statistical measures
   - Visualizations (interactive Plotly or static Seaborn/Matplotlib)
   - Data quality alerts (column-level)
   
3. **Sample Data**: Head and tail sample rows
   - First 10 rows of the dataset (HTML table)
   - Last 10 rows of the dataset (HTML table)
   
4. **Correlations**: Correlation matrices and heatmaps
   - Pearson correlation (numerical variables)
   - Spearman correlation (numerical variables)
   - Cramér's V (categorical variables)
   - Visual heatmaps (when include_correlations_plots is True)
   - JSON data (when include_correlations_json is True)

The report is fully interactive with Bootstrap styling, allowing for:
- Collapsible sections for better organization
- Sortable tables for data exploration
- Interactive visualizations (when use_plotly is True)
- Responsive design that works on desktop and mobile devices
- Clean, professional appearance with color-coded alerts

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
        Analyze a single column of data (internal method).
        
        Parameters:
        -----------
        column_data : pandas.Series
            The column data to analyze
        column_name : str
            The name of the column
            
        Returns:
        --------
        dict
            Dictionary of analysis results for the column containing:
            - Data_type: pandas dtype as string
            - missing_values: count of missing values
            - missing_%: percentage of missing values
            - Type-specific statistics (varies by column type)
            - plot: visualization data (when include_plots is True)
            - plot_bar: additional bar chart for text columns (when applicable)
            - alerts: data quality alerts (when include_alerts is True)
        """
        
    def _data_sample(self):
        """
        Create HTML samples of the dataset head and tail (internal method).
        
        Returns:
        --------
        dict
            Dictionary with HTML representations:
            - 'Head': HTML table of first 10 rows
            - 'Tail': HTML table of last 10 rows
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
        Include data quality alerts
    
    include_sample_data : bool, default=True
        Include head/tail data samples
    
    include_overview : bool, default=True
        Include dataset overview statistics
    """
```
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

You can extend the library by registering custom analyzers for specific data types using the decorator-based registry system:

```python
from data_visualizer.type_registry import register_analyzer
from visions.types import DateTime
import pandas as pd

@register_analyzer(DateTime)
def _analyze_datetime(report_object, column_data):
    """
    Custom analyzer for datetime columns.
    
    Parameters:
    -----------
    report_object : AnalysisReport
        The AnalysisReport instance (provides access to settings)
    column_data : pandas.Series
        The datetime column to analyze
        
    Returns:
    --------
    dict
        Dictionary of datetime-specific statistics
    """
    datetime_stats = {
        'min_date': str(column_data.min()),
        'max_date': str(column_data.max()),
        'range_days': (column_data.max() - column_data.min()).days,
        'weekday_counts': column_data.dt.day_name().value_counts().to_dict()
    }
    return datetime_stats
```

### How the Type Registry Works

1. **Registration**: The `@register_analyzer(VisionType)` decorator registers a function in the `analyzer_registry` dictionary
2. **Type Detection**: When analyzing a column, the library uses `visions.CompleteSet` to infer the column's type
3. **Lookup**: The inferred type is used to look up the appropriate analyzer function from the registry
4. **Execution**: The analyzer function is called with `(report_object, column_data)` parameters
5. **Fallback**: If no analyzer is registered for a type, `_analyse_generic` is used as fallback

### Built-in Type Analyzers

The library includes pre-registered analyzers for:
- **Float, Integer, Numeric**: `_analyse_numeric` - statistical measures, outliers, skewness, kurtosis
- **Object, Categorical**: `_analyse_category` - value counts, cardinality, top N values
- **String**: `_analyse_string` - value counts, cardinality, word frequency analysis
- **Boolean**: `_analyse_boolean` - value counts and proportions
- **Generic**: `_analyse_generic` - basic unique value count (fallback)

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
