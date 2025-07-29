import pandas as pd
from visions.typesets import VisionsTypeset  #used to get the types







def _analyse_numeric(self, column_data):
        numeric_stats = column_data.describe().to_dict()
        
        return numeric_stats
    
def _analyse_category(self,column_data):
    
    categorical_stats={}
    
    num_unique = column_data.nunique()
    categorical_stats['unique_values'] = num_unique
    
    if num_unique>50:
        
        categorical_stats['cardinality']= 'High'
    else:
        categorical_stats['cardinality']= 'Low'

    top_5_counts = column_data.value_counts().nlargest(5).to_dict()
    categorical_stats['value_counts_top_10'] = top_5_counts
    
    return categorical_stats
    
    
def _analyse_boolean(self,column_data):
    value_counts = column_data.value_counts().to_dict()
    
    bool_stats = {
        'value_counts': value_counts
    }
    
    return bool_stats
    
    
