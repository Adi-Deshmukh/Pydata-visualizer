import pandas as pd
from DataAnalyser.profiler import AnalysisReport, Settings 
from DataAnalyser.report import generate_html_report
import pprint


print("Script started successfully!")
print("Attempting to create a DataFrame...")

'''
# Create a simple DataFrame for testing
data = {'col1': [1, 2, 3, 2], 'col2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)
'''

#df = pd.read_csv(r"C:\Users\kiran\Downloads\netflix.csv")
df = pd.read_csv(r"C:\Users\kiran\final_vg.csv")

print("DataFrame created.")
print("Attempting to create an AnalysisReport object...")

report_settings = Settings(
    minimal=True,          #  want a fast report
    top_n_values=3,        #  the top 3 values
    skewness_threshold=2.0 #  tolerance for skewness
)

# Create an instance of your class
report = AnalysisReport(df, settings=report_settings)

result_dict = report.analyse()


print("--- Full Analysis Results ---")

generate_html_report(result_dict)