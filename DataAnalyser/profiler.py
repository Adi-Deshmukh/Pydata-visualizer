import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from .visualizer import get_plot_as_base64 


class AnalysisReport:
    
    
    def __init__(self,data):
        self.data = data

    def analyse(self):
        num_rows = self.data.shape[0] 
        num_columns = self.data.shape[1] 
        num_duplicates = self.data.duplicated().sum()
        
        overview_stats = {
        'num_Row': num_rows,
        'num_Columns': num_columns,
        'duplicated_rows': int(num_duplicates)
        }
    
        variable_stats = {}
        columns = self.data.columns
        
        for column_name in columns:
            
            column_data = self.data[column_name] 
            
            single_column_analysis = self._analyze_column(column_data,column_name)
            
            variable_stats[column_name] = single_column_analysis
    
        final_results = {
            'overview': overview_stats,
            'variables': variable_stats 
        }
        
        return final_results 

    
    def _analyze_column(self,column_data,column_name):
        
        dtype = column_data.dtype
        missing_vals = column_data.isna().sum()
        missing_percentage = (column_data.isna().sum()/self.data.shape[0])*100
        
        column_details = {
            'Data_type': str(dtype),
            'missing_values': int(missing_vals),
            'missing_%': float(missing_percentage)
        }
        
        
        if pd.api.types.is_numeric_dtype(column_data):
            description = column_data.describe().to_dict()
            column_details.update(description)
        else:
            num_unique = column_data.nunique()
            column_details['unique_values'] = num_unique
            if num_unique > 50:
                
                #high cardinality columns
                
                value_counts_dict = column_data.value_counts().nlargest(5).to_dict()
                column_details['value_counts_top_5'] = value_counts_dict
                
            else:
                
                #for low cardinality columns
            
                value_counts_dict = column_data.value_counts().to_dict()
                column_details['value_counts'] = value_counts_dict
            
            
        plot_string = get_plot_as_base64(column_data, column_name)
        column_details['plot_base64'] = plot_string
        
            
        return column_details
        