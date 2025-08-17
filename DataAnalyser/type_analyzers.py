import pandas as pd
from visions.typesets import VisionsTypeset  #used to get the types


def _analyse_numeric(report_object, column_data):
        numeric_stats = column_data.describe().to_dict()
        
        # calculate skewness in data and add it
        numeric_stats['skewness'] = column_data.skew()
    
        # calculate kurtosis and add it
        numeric_stats['kurtosis'] = column_data.kurt()
            
        return numeric_stats
    
def _analyse_category(report_object,column_data):
    
    categorical_stats={}
    
    num_unique = column_data.nunique()
    categorical_stats['unique_values'] = num_unique
    
    if num_unique>50:
        
        categorical_stats['cardinality']= 'High'
    else:
        categorical_stats['cardinality']= 'Low'

    top_n_counts = column_data.value_counts().nlargest(report_object.settings.top_n_values).to_dict()
    categorical_stats['value_counts_top_n'] = top_n_counts

    return categorical_stats


def _analyse_boolean(report_object,column_data):
    value_counts = column_data.value_counts().to_dict()
    
    bool_stats = {
        'value_counts': value_counts
    }
    
    return bool_stats
    
    
