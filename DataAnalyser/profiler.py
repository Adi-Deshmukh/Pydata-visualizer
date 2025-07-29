import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from visions.typesets import CompleteSet  #used to get the types
from .type_analyzers import _analyse_numeric,_analyse_category,_analyse_boolean
from visions.types import Numeric, Boolean, Categorical
from .visualizer import get_plot_as_base64 



class AnalysisReport:
    
    
    def __init__(self,data, minimal=False):
        self.data = data
        self.minimal = minimal 
        self.typeset = CompleteSet()

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
            
            variable_stats[column_name] = single_column_analysis # This is the column_details
        
        sample_data = self._data_sample()
    
        final_results = {
            'overview': overview_stats,
            'variables': variable_stats,
            'Sample_data': sample_data
        }
        
        
        
        return final_results 

    # used to get the details of a single columns
    def _analyze_column(self,column_data,column_name):
        
        dtype = column_data.dtype
        missing_vals = column_data.isna().sum()
        missing_percentage = (column_data.isna().sum()/self.data.shape[0])*100
        
        column_details = {
            'Data_type': str(dtype),
            'missing_values': int(missing_vals),
            'missing_%': float(missing_percentage)
        }        
        
        if not self.minimal:
        
            inferred_type = self.typeset.infer_type(column_data)
            
            type_dispatcher = {
                Numeric: _analyse_numeric, # we add the references to the specialist functions
                Categorical: _analyse_category,
                Boolean: _analyse_boolean
            }
            
            analyzer_function = type_dispatcher.get(inferred_type,_analyse_category) # Getting the Right Function
            
            type_specific_stats = analyzer_function(self,column_data)
            
            column_details.update(type_specific_stats)
            
            # used to pass the arguments to the visualizer.py to get the plot  
            plot_string = get_plot_as_base64(column_data, column_name)
            column_details['plot_base64'] = plot_string
                
            
        return column_details

    
    def _data_sample(self):
        
        head_10 = self.data.head(10).to_html()
        tail_10 = self.data.tail(10).to_html()
        
        sample_data = {
            'Head': head_10,
            'Tail': tail_10
        }
        
        return sample_data
    

