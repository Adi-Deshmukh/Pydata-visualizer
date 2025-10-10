import pandas as pd
import numpy as np
from visions.typesets import VisionsTypeset  #used to get the types
from visions.types import Numeric, Boolean, Categorical, String, Object, Float, Integer
from .type_registry import register_analyzer
from collections import Counter



'''
    Detect outliers using IQR method.
    
    Args:
        column_data: pandas Series with numeric data
        threshold: IQR multiplier (e.g., 1.5 for standard bounds)
    
    Returns:
        Dict with outlier_count, outlier_percentage, and outliers list
    '''

def _detect_outliers_iqr(column_data: pd.Series, threshold: float) -> dict:
    
    if column_data.empty or not pd.api.types.is_numeric_dtype(column_data):
        return {'outlier_count': 0, 'outlier_percentage': 0.0, 'outliers': []}
    
    Q1 = column_data.quantile(0.25)
    Q3 = column_data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    
    outlier_mask = (column_data < lower_bound) | (column_data > upper_bound)
    outlier_indices = column_data[outlier_mask].index.tolist()
    outlier_count = len(outlier_indices)
    total_count = len(column_data)
    outlier_percentage = (outlier_count / total_count * 100) if total_count > 0 else 0.0
    
    return {
        'outlier_count': outlier_count,
        'outlier_percentage': outlier_percentage,
        'outlier_indices': outlier_indices  # For graph highlighting only
    }

@register_analyzer(Float)
@register_analyzer(Integer)
@register_analyzer(Numeric)
def _analyse_numeric(report_object, column_data):
    numeric_stats = column_data.describe().to_dict()
    
    # calculate skewness in data and add it
    numeric_stats['skewness'] = float(column_data.skew()) if not pd.isna(column_data.skew()) else 0.0

    # calculate kurtosis and add it
    numeric_stats['kurtosis'] = float(column_data.kurt()) if not pd.isna(column_data.kurt()) else 0.0
        
    # Add outlier detection using settings threshold
    outlier_info = _detect_outliers_iqr(column_data, report_object.settings.outlier_threshold)
    numeric_stats.update(outlier_info)
    
    return numeric_stats


@register_analyzer(Object)
@register_analyzer(Categorical)
def _analyse_category(report_object,column_data):
    
    categorical_stats={}
    
    num_unique = column_data.nunique()
    categorical_stats['unique_values'] = num_unique
    
    # Safe handling of mode for empty or all-null columns
    if not column_data.empty and column_data.dropna().shape[0] > 0:
        categorical_stats['most_frequent'] = column_data.mode().iloc[0]
    else:
        categorical_stats['most_frequent'] = None
    
    if num_unique>50:
        categorical_stats['cardinality']= 'High'
    else:
        categorical_stats['cardinality']= 'Low'

    top_n_counts = column_data.value_counts().nlargest(report_object.settings.top_n_values).to_dict()
    categorical_stats['value_counts_top_n'] = top_n_counts

    return categorical_stats

@register_analyzer(Boolean)
def _analyse_boolean(report_object,column_data):
    value_counts = column_data.value_counts().to_dict()
    
    bool_stats = {
        'value_counts': value_counts
    }
    
    return bool_stats


@register_analyzer(String)
def _analyse_string(report_object, column_data: pd.Series) -> dict:
    string_stats = {
        'num_unique': column_data.nunique(),
        'most_frequent': column_data.mode().iloc[0] if not column_data.empty else None,
        'cardinality': 'High' if column_data.nunique() > 50 else 'Low',
        'value_counts_top_n': column_data.value_counts().nlargest(report_object.settings.top_n_values).to_dict()
    }

    if report_object.settings.text_analysis:
        words = ' '.join(column_data.dropna().astype(str)).split()
        word_freq = Counter(words).most_common(10)
        string_stats['word_frequencies'] = dict(word_freq)

    return string_stats

def _analyse_generic(report_object,column_data):
    generic_stats = {
        'num_unique': str(column_data.nunique()),
        
    }

    return generic_stats

