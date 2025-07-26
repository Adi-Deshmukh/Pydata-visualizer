import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
            
            single_column_analysis = self._analyze_column(column_data)
            
            variable_stats[column_name] = single_column_analysis
    
        final_results = {
            'overview': overview_stats,
            'variables': variable_stats 
        }
        
        return final_results 

    
    def _analyze_column(self,column_data):
        
        
        dtype = column_data.dtype
        missing_vals = column_data.isna().sum()
        missing_percentage = (column_data.isna().sum()/self.data.shape[0])*100
        
        column_details = {
            'Data_type': str(dtype),
            'missing_values': int(missing_vals),
            'missing_%': float(missing_percentage)
        }
            
        return column_details
        