

import pandas as pd
from DataAnalyser.profiler import AnalysisReport, Settings 
from DataAnalyser.report import generate_html_report


print("Script started successfully!")




#df = pd.read_csv(r"C:\Users\kiran\Downloads\netflix.csv")
df = pd.read_csv(r"C:\Users\kiran\final_vg.csv")

report_settings = Settings(
    minimal=True,          #  want a fast report
    top_n_values=3,        #  the top 3 values
    skewness_threshold=2.0 #  tolerance for skewness
)

# Create an instance of your class
report = AnalysisReport(df, settings=report_settings)

result_dict = report.analyse()


generate_html_report(result_dict)