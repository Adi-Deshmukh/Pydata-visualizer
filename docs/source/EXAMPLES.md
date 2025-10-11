# Pydata-visualizer Examples

This document provides various examples of how to use Pydata-visualizer in different scenarios.

## Table of Contents

1. [Basic Usage](#basic-usage)
2. [Customizing Analysis](#customizing-analysis)
3. [Working with Different Data Types](#working-with-different-data-types)
4. [Processing Large Datasets](#processing-large-datasets)
5. [Accessing Results Programmatically](#accessing-results-programmatically)
6. [Integration Examples](#integration-examples)
7. [Common Workflows](#common-workflows)

## Basic Usage

### Simple Analysis and Report Generation

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load sample data
df = pd.read_csv("sample_data.csv")

# Create and generate report
report = AnalysisReport(df)
report.to_html("basic_report.html")
```

### Loading Data from Different Sources

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# From CSV
df_csv = pd.read_csv("data.csv")
report_csv = AnalysisReport(df_csv)
report_csv.to_html("csv_report.html")

# From Excel
df_excel = pd.read_excel("data.xlsx", sheet_name="Sheet1")
report_excel = AnalysisReport(df_excel)
report_excel.to_html("excel_report.html")

# From database using SQL
import sqlite3
conn = sqlite3.connect("database.db")
df_sql = pd.read_sql_query("SELECT * FROM table_name", conn)
report_sql = AnalysisReport(df_sql)
report_sql.to_html("sql_report.html")

# From JSON
df_json = pd.read_json("data.json")
report_json = AnalysisReport(df_json)
report_json.to_html("json_report.html")
```

## Customizing Analysis

### Using Settings to Configure Analysis

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport, Settings

# Load data
df = pd.read_csv("customer_data.csv")

# Custom settings
settings = Settings(
    minimal=False,              # Full analysis with all features
    top_n_values=5,             # Show top 5 values in categorical columns
    skewness_threshold=1.5,     # Lower threshold for skewness alerts
    outlier_method='iqr',       # Use IQR method for outlier detection
    outlier_threshold=1.5,      # Standard IQR multiplier
    duplicate_threshold=3.0,    # Alert if duplicates exceed 3%
    text_analysis=True          # Enable word cloud and frequency analysis
)

# Create and generate report with custom settings
report = AnalysisReport(df, settings=settings)
report.to_html("custom_report.html")
```

### Minimal Analysis for Quick Overview

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport, Settings

# Load data
df = pd.read_csv("large_dataset.csv")

# Minimal settings for fast processing
minimal_settings = Settings(minimal=True)

# Create and generate quick report
quick_report = AnalysisReport(df, settings=minimal_settings)
quick_report.to_html("quick_overview.html")
```

## Working with Different Data Types

### Mixed Data Types Analysis

```python
import pandas as pd
import numpy as np
from data_visualizer.profiler import AnalysisReport

# Create a dataset with mixed types
data = {
    'numeric': np.random.normal(0, 1, 1000),
    'categorical': np.random.choice(['A', 'B', 'C', 'D'], 1000),
    'boolean': np.random.choice([True, False], 1000),
    'datetime': pd.date_range('2023-01-01', periods=1000),
    'text': ['Text sample ' + str(i) for i in range(1000)]
}
df = pd.DataFrame(data)

# Create and generate report
mixed_report = AnalysisReport(df)
mixed_report.to_html("mixed_types_report.html")
```

### Financial Data Analysis

```python
import pandas as pd
import numpy as np
from data_visualizer.profiler import AnalysisReport, Settings

# Create sample financial data
np.random.seed(42)
data = {
    'date': pd.date_range('2022-01-01', periods=100),
    'price': np.random.normal(100, 15, 100).cumsum() + 1000,
    'volume': np.random.randint(1000, 100000, 100),
    'change_pct': np.random.normal(0, 1, 100),
    'sector': np.random.choice(['Tech', 'Finance', 'Healthcare', 'Energy'], 100)
}
financial_df = pd.DataFrame(data)

# Settings for financial analysis (higher skewness tolerance)
financial_settings = Settings(skewness_threshold=3.0, outlier_threshold=3.0)

# Create and generate report
financial_report = AnalysisReport(financial_df, settings=financial_settings)
financial_report.to_html("financial_report.html")
```

## Text Data Analysis

### Analyzing Text Columns with Word Clouds

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport, Settings

# Create sample dataset with text reviews
df = pd.DataFrame({
    'product_id': range(1, 101),
    'customer_review': [
        'excellent product quality amazing', 'good value for money',
        'poor customer service disappointed', 'fast delivery great experience',
        'highly recommend excellent', 'defective item bad quality'
    ] * 16 + ['great product'] * 4,
    'rating': [5, 4, 2, 5, 5, 1] * 16 + [5] * 4
})

# Enable text analysis for word clouds
settings = Settings(text_analysis=True, top_n_values=10)

# Create report - will generate word clouds for text columns
report = AnalysisReport(df, settings=settings)
report.to_html("text_analysis_report.html")

# Word clouds will show frequently occurring words in the reviews
# Bar charts will show the most common complete review texts
```

### Disabling Text Analysis for Performance

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport, Settings

# For datasets with many text columns, disable text analysis for faster processing
settings = Settings(text_analysis=False)

# Create report without word frequency analysis
report = AnalysisReport(large_text_df, settings=settings)
report.to_html("no_text_analysis_report.html")
```

## Processing Large Datasets

### Using Sampling for Large Datasets

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport, Settings

# Load large dataset
large_df = pd.read_csv("large_dataset.csv")

# Sample the dataset for faster processing
sampled_df = large_df.sample(n=10000, random_state=42)

# Create report with sampled data
sampled_report = AnalysisReport(sampled_df)
sampled_report.to_html("sampled_report.html")
```

### Analyzing Specific Columns Only

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load large dataset
large_df = pd.read_csv("large_dataset.csv")

# Select only important columns
important_columns = ['customer_id', 'purchase_amount', 'product_category', 'purchase_date']
subset_df = large_df[important_columns]

# Create report with subset of columns
subset_report = AnalysisReport(subset_df)
subset_report.to_html("important_columns_report.html")
```

## Accessing Results Programmatically

### Getting Analysis Results as Python Objects

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load data
df = pd.read_csv("survey_data.csv")

# Create report and run analysis
report = AnalysisReport(df)
results = report.analyse()

# Access various components of the results
overview = results['overview']
variables = results['variables']
correlations = results['Correlations_JSON']

# Print some insights
print(f"Dataset has {overview['num_Row']} responses with {overview['missing_percentage']:.2f}% missing data")

# Check for highly skewed variables
skewed_variables = []
for var_name, var_stats in variables.items():
    if 'skewness' in var_stats and abs(var_stats['skewness']) > 2.0:
        skewed_variables.append((var_name, var_stats['skewness']))

print(f"Found {len(skewed_variables)} highly skewed variables:")
for var, skew in skewed_variables:
    print(f"- {var}: {skew:.2f}")

# Find strongly correlated pairs
if 'pearson' in correlations:
    pearson = pd.DataFrame(correlations['pearson'])
    strong_correlations = []
    
    for i in range(len(pearson.columns)):
        for j in range(i+1, len(pearson.columns)):
            if abs(pearson.iloc[i, j]) > 0.7:
                strong_correlations.append((
                    pearson.columns[i], 
                    pearson.columns[j], 
                    pearson.iloc[i, j]
                ))
    
    print(f"Found {len(strong_correlations)} strongly correlated pairs:")
    for var1, var2, corr in strong_correlations:
        print(f"- {var1} & {var2}: {corr:.3f}")
```

### Extracting Visualizations from Results

```python
import pandas as pd
import matplotlib.pyplot as plt
import base64
from data_visualizer.profiler import AnalysisReport
import io

# Load data
df = pd.read_csv("product_data.csv")

# Create report and run analysis
report = AnalysisReport(df)
results = report.analyse()

# Extract and save a specific column's visualization
if 'price' in results['variables']:
    price_info = results['variables']['price']
    if 'plot_base64' in price_info:
        # Extract the base64 image data (remove header info)
        img_data = price_info['plot_base64'].split(',')[1]
        
        # Decode and save to file
        with open("price_distribution.png", "wb") as f:
            f.write(base64.b64decode(img_data))
        
        print("Saved price distribution plot as price_distribution.png")
        
# Extract and save correlation heatmap
if 'pearson' in results['Correlations_Plots']:
    # Extract the base64 image data (remove header info)
    img_data = results['Correlations_Plots']['pearson'].split(',')[1]
    
    # Decode and save to file
    with open("correlation_heatmap.png", "wb") as f:
        f.write(base64.b64decode(img_data))
    
    print("Saved correlation heatmap as correlation_heatmap.png")
```

## Integration Examples

### Integrating with Web Applications (Flask)

```python
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from data_visualizer.profiler import AnalysisReport
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['REPORT_FOLDER'] = 'static/reports'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['REPORT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Generate a unique report name
            report_name = f"report_{filename.split('.')[0]}.html"
            report_path = os.path.join(app.config['REPORT_FOLDER'], report_name)
            
            # Process the file based on extension
            if filename.endswith('.csv'):
                df = pd.read_csv(filepath)
            elif filename.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(filepath)
            else:
                return "Unsupported file format"
            
            # Generate report
            report = AnalysisReport(df)
            report.to_html(report_path)
            
            return redirect(url_for('show_report', report_name=report_name))
    
    return '''
    <!doctype html>
    <title>Upload Data for Analysis</title>
    <h1>Upload your data file</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file accept=".csv,.xls,.xlsx">
      <input type=submit value=Analyze>
    </form>
    '''

@app.route('/report/<report_name>')
def show_report(report_name):
    return redirect(f'/static/reports/{report_name}')

if __name__ == '__main__':
    app.run(debug=True)
```

### Integration with Jupyter Notebooks

```python
import pandas as pd
import matplotlib.pyplot as plt
from data_visualizer.profiler import AnalysisReport, Settings
import webbrowser
import os
from IPython.display import IFrame, display, HTML

# Load data
df = pd.read_csv("dataset.csv")

# Create report with custom settings
settings = Settings(top_n_values=7, skewness_threshold=1.5)
report = AnalysisReport(df, settings=settings)

# Generate HTML report
report_path = "notebook_report.html"
report.to_html(report_path)

# For inline preview in the notebook
display(HTML(f'<a href="{report_path}" target="_blank">Click to open full report</a>'))

# Show report in an iframe (limited functionality)
display(IFrame(src=report_path, width=800, height=600))

# Alternatively, open in a browser
full_path = os.path.abspath(report_path)
webbrowser.open(f'file://{full_path}')
```

## Common Workflows

### Data Cleaning Workflow

```python
import pandas as pd
import numpy as np
from data_visualizer.profiler import AnalysisReport

# Load messy data
df_messy = pd.read_csv("messy_data.csv")

# Step 1: Initial profiling to identify issues
initial_report = AnalysisReport(df_messy)
results = initial_report.analyse()
initial_report.to_html("initial_report.html")

# Step 2: Clean data based on profiling results
df_clean = df_messy.copy()

# Handle missing values
missing_cols = []
for col, stats in results['variables'].items():
    if stats['missing_%'] > 0:
        missing_cols.append((col, stats['missing_%']))

print("Columns with missing values:")
for col, pct in sorted(missing_cols, key=lambda x: x[1], reverse=True):
    print(f"- {col}: {pct:.2f}%")
    
    # Fill or drop based on missing percentage
    if pct > 50:
        print(f"  Dropping column {col} due to high missing rate")
        df_clean = df_clean.drop(columns=[col])
    elif pd.api.types.is_numeric_dtype(df_clean[col]):
        print(f"  Filling {col} with median")
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())
    else:
        print(f"  Filling {col} with mode")
        df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

# Handle extreme outliers in numeric columns
for col, stats in results['variables'].items():
    if col in df_clean and pd.api.types.is_numeric_dtype(df_clean[col]):
        if 'skewness' in stats and abs(stats['skewness']) > 3:
            print(f"Handling outliers in {col} (skewness: {stats['skewness']:.2f})")
            q1 = stats.get('25%', df_clean[col].quantile(0.25))
            q3 = stats.get('75%', df_clean[col].quantile(0.75))
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            
            # Cap outliers
            df_clean[col] = df_clean[col].clip(lower_bound, upper_bound)

# Step 3: Profile the cleaned data
final_report = AnalysisReport(df_clean)
final_report.to_html("cleaned_data_report.html")

# Save cleaned data
df_clean.to_csv("cleaned_data.csv", index=False)
print(f"Cleaned data saved with {df_clean.shape[0]} rows and {df_clean.shape[1]} columns")
```

### Feature Selection Workflow

```python
import pandas as pd
import numpy as np
from data_visualizer.profiler import AnalysisReport

# Load dataset with many features
df = pd.read_csv("features_dataset.csv")

# Assume the target column name is 'target'
features = df.drop(columns=['target'])
target = df['target']

# Step 1: Profile the data
report = AnalysisReport(df)
results = report.analyse()

# Step 2: Filter columns based on profiling insights
selected_features = []

# Remove columns with high missing values
for col, stats in results['variables'].items():
    if col != 'target' and stats['missing_%'] < 20:
        selected_features.append(col)

print(f"After removing high-missing columns: {len(selected_features)} features left")

# Filter out highly correlated features
if 'pearson' in results['Correlations_JSON']:
    pearson = pd.DataFrame(results['Correlations_JSON']['pearson'])
    
    # Find pairs of highly correlated features
    correlated_pairs = []
    for i, col1 in enumerate(selected_features):
        for col2 in selected_features[i+1:]:
            if col1 in pearson and col2 in pearson:
                correlation = abs(pearson.loc[col1, col2])
                if correlation > 0.85:  # High correlation threshold
                    correlated_pairs.append((col1, col2, correlation))
    
    # Sort by correlation strength
    correlated_pairs.sort(key=lambda x: x[2], reverse=True)
    
    # Remove one feature from each highly correlated pair
    removed_features = set()
    for col1, col2, corr in correlated_pairs:
        if col1 not in removed_features and col2 not in removed_features:
            # Keep the one with lower missing value percentage
            if results['variables'][col1]['missing_%'] > results['variables'][col2]['missing_%']:
                removed_features.add(col1)
            else:
                removed_features.add(col2)
    
    for feature in removed_features:
        if feature in selected_features:
            selected_features.remove(feature)

print(f"After removing highly correlated features: {len(selected_features)} features left")

# Create a new dataset with selected features
selected_df = df[selected_features + ['target']]

# Profile the reduced feature set
reduced_report = AnalysisReport(selected_df)
reduced_report.to_html("reduced_features_report.html")

# Save the dataset with selected features
selected_df.to_csv("selected_features.csv", index=False)
```

These examples demonstrate various ways to use Pydata-visualizer in real-world scenarios. You can adapt them to your specific needs and data types.
