import pandas as pd
# Import both classes from your library
from data_visualizer.profiler import AnalysisReport
from data_visualizer.report import generate_html_report # <-- ADD THIS IMPORT

print("--- Starting Test ---")

df = pd.read_csv(r"C:\Users\kiran\final_vg.csv")

try:
    # Step 1: Perform the analysis
    report_analyzer = AnalysisReport(df)
    analysis_results = report_analyzer.analyse()
    print("--- Analysis Complete ---")

    # Step 2: Generate the HTML report from the results
    generate_html_report(analysis_results)
    print("--- Report Generated Successfully ---")

except Exception as e:
    print(f"An error occurred: {e}")

print("--- Test Finished ---")