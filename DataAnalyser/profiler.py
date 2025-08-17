import pandas as pd
import pydantic
from visions.typesets import CompleteSet  #used to get the types
from .type_analyzers import _analyse_numeric,_analyse_category,_analyse_boolean
from visions.types import Numeric, Boolean, Categorical
from .alerts import generate_alerts
from .visualizer import get_plot_as_base64
from .correlations import calculate_correlations,generate_correlation_heatmap



class Settings(pydantic.BaseModel):
    """
    Settings for the analysis report.
    """
    minimal: bool = False
    top_n_values: int = 10
    skewness_threshold: float = 1.0


class AnalysisReport:    

    def __init__(self,data, settings: Settings = None):
        self.data = data
        self.settings = settings or Settings()
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
        
        sample_data = self._data_sample() # Used to show Head, Tail of the Dataset
        
        correlations = calculate_correlations(self.data) # Getting correlation Values

        correlations_plots = {}   # We created this separately so that we don't overwrite the actual number data/raw data in correlations 
        correlations_json = {} # we create this to solve the type error 
        for key,value in correlations.items():
            if isinstance(value, pd.DataFrame) and value.shape[0] > 1:
                correlations_plots[key] = generate_correlation_heatmap(value)
                correlations_json[key] = value.to_dict() # Convert DataFrame to JSON-compatible format for index.html

        final_results = {
            'overview': overview_stats,
            'variables': variable_stats,
            'Sample_data': sample_data,
            'Correlations_Plots': correlations_plots, 
            'Correlations_JSON': correlations_json 
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

    # Generate alerts for the column
        alert_details = generate_alerts(column_details)
        column_details['alerts'] = alert_details


        if not self.settings.minimal: # If minimal is False, we perform basic analysis

            inferred_type = self.typeset.infer_type(column_data)
            # We use the inferred type to determine which analysis function to call
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
    


