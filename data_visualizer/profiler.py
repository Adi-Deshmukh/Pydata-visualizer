import warnings

# This will suppress all FutureWarnings
warnings.filterwarnings('ignore', category=FutureWarning)

# This will suppress all UserWarnings
warnings.filterwarnings('ignore', category=UserWarning)


import pandas as pd
import pydantic
from pydantic import Field
from visions.typesets import CompleteSet  #used to get the types
from .type_analyzers import  _analyse_generic
from .type_registry import analyzer_registry
from .alerts import generate_alerts, generate_dataset_alerts
from .visualizer import get_plot_as_base64
from .correlations import calculate_correlations,generate_correlation_heatmap
from .report import generate_html_report 
from .settings import Settings
from tqdm import tqdm
from colorama import Fore, Style, init
from visions.types import Float, Integer
init(autoreset=True)  # This makes sure each print statement resets to the default color

class AnalysisReport:    

    def __init__(self,data, settings: Settings = None):
        self.data = data
        self.settings = settings or Settings()
        self.typeset = CompleteSet()
        self.results = None

    def analyse(self):
        """
        Analyze the dataset and return a dictionary of results.
        """
        print(Fore.GREEN + "Starting analysis..." + Style.BRIGHT)
        print(Fore.YELLOW + "Attempting to create an AnalysisReport object..." + Style.BRIGHT)

        num_rows = self.data.shape[0]
        num_columns = self.data.shape[1]
        num_duplicates = self.data.duplicated().sum()
        duplicate_percentage = (num_duplicates / num_rows * 100) if num_rows > 0 else 0.0
        duplicate_indices = self.data.index[self.data.duplicated()].tolist()
        duplicate_samples = self.data[self.data.duplicated(keep=False)].head(5).to_dict('records')

        overview_stats = {
            'num_Row': num_rows,
            'num_Columns': num_columns,
            'duplicated_rows': int(num_duplicates),
            'duplicate_percentage': float(duplicate_percentage),
            'duplicate_indices': duplicate_indices,
            'duplicate_samples': duplicate_samples,
            'missing_values': int(self.data.isna().sum().sum()),
            'missing_percentage': float(self.data.isna().sum().sum() / (num_rows * num_columns) * 100) if num_rows * num_columns > 0 else 0.0,
            'alerts': generate_dataset_alerts(
                {'duplicate_percentage': duplicate_percentage},
                settings=self.settings
            )
        }

        variable_stats = {}
        columns = self.data.columns

        for column_name in tqdm(columns, desc="Analyzing columns", unit="column"):
            column_data = self.data[column_name]
            single_column_analysis = self._analyze_column(column_data, column_name)
            variable_stats[column_name] = single_column_analysis

        sample_data = self._data_sample()

        correlations = calculate_correlations(self.data)

        correlations_plots = {}
        correlations_json = {}
        if correlations:
            for key, value in correlations.items():
                if isinstance(value, pd.DataFrame) and value.shape[0] > 1:
                    correlations_plots[key] = generate_correlation_heatmap(value)
                    correlations_json[key] = value.to_dict()

        final_results = {
            'overview': overview_stats,
            'variables': variable_stats,
            'Sample_data': sample_data,
            'Correlations_Plots': correlations_plots,
            'Correlations_JSON': correlations_json
        }

        print(Fore.GREEN + "--- Full Analysis Done ---" + Style.BRIGHT)
        self.results = final_results
        return final_results
    
    def to_html(self, filename="report.html"):
        """
        A convenience method that runs the analysis and generates the HTML report.
        """
        # First, make sure the analysis has been run
        if self.results is None:
            print("Performing analysis...")
            self.analyse()
        generate_html_report(self.results, filename)
    

    # used to get the details of a single columns
    from visions.types import Float, Integer  # Add to imports

    def _analyze_column(self, column_data, column_name):
        """
        Analyze a single column and return its details.
        """
        dtype = column_data.dtype
        missing_vals = column_data.isna().sum()
        missing_percentage = (missing_vals / self.data.shape[0]) * 100

        column_details = {
            'Data_type': str(dtype),
            'missing_values': int(missing_vals),
            'missing_%': float(missing_percentage)
        }

        if not self.settings.minimal:
            inferred_type = self.typeset.infer_type(column_data)
            registry_func = analyzer_registry.get(inferred_type, _analyse_generic)
            column_details.update(registry_func(self, column_data))
            
            # Get outlier indices for numeric columns (for graph highlighting)
            outlier_indices = column_details.get('outlier_indices', []) if inferred_type in [Float, Integer] else None
            
            # Get word frequencies for string columns (for word cloud)
            word_frequencies = column_details.get('word_frequencies', None)
            
            # Generate main plot (distribution for numeric/categorical, or word cloud for text)
            column_details['plot_base64'] = get_plot_as_base64(
                column_data, 
                column_name, 
                outliers=outlier_indices,
                word_frequencies=word_frequencies
            )
            
            # If word frequencies exist and not empty, also generate a bar chart for value counts
            if word_frequencies and len(word_frequencies) > 0:
                column_details['plot_bar_base64'] = get_plot_as_base64(
                    column_data,
                    column_name,
                    outliers=None,
                    word_frequencies=None  # Force bar chart
                )
            
            # Remove outlier_indices from output (only needed for plotting)
            column_details.pop('outlier_indices', None)

        # Generate alerts for the column (AFTER type-specific analysis to include outlier stats)
        alert_details = generate_alerts(column_details, settings=self.settings)  # Pass settings
        column_details['alerts'] = alert_details

        return column_details

    
    def _data_sample(self):
        
        head_10 = self.data.head(10).to_html()
        tail_10 = self.data.tail(10).to_html()
        
        sample_data = {
            'Head': head_10,
            'Tail': tail_10
        }
        
        
        return sample_data
    
    



