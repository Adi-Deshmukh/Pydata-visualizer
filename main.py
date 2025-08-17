import pandas as pd
from DataAnalyser.profiler import AnalysisReport 
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

# Create an instance of your class
report = AnalysisReport(df)

result_dict = report.analyse()


print("--- Full Analysis Results ---")

generate_html_report(result_dict)