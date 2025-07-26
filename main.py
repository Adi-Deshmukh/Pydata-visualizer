import pandas as pd
from mylib.profiler import AnalysisReport 

print("Script started successfully!")
print("Attempting to create a DataFrame...")

'''
# Create a simple DataFrame for testing
data = {'col1': [1, 2, 3, 2], 'col2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)
'''

df= df = pd.read_csv(r"C:\Users\kiran\Downloads\netflix.csv")

print("DataFrame created.")
print("Attempting to create an AnalysisReport object...")

# Create an instance of your class
report = AnalysisReport(df)

result_dict = report.analyse()


print("AnalysisReport object created successfully!")
print("The 'report' object is holding a DataFrame with stats:", result_dict)