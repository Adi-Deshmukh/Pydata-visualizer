

import pandas as pd
from data_visualizer.profiler import AnalysisReport, Settings 
from data_visualizer.report import generate_html_report



#df = pd.read_csv(r"C:\Users\kiran\Downloads\netflix.csv")
df = pd.read_csv(r"C:\Users\kiran\final_vg.csv")

report_settings = Settings(
    minimal=False,          #  want a fast report
    top_n_values=3,        #  the top 3 values
    skewness_threshold=2.0 #  tolerance for skewness
)

# Create an instance of your class
report = AnalysisReport(df, settings=report_settings)

report.to_html(filename="report.html")