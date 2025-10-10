import pandas as pd
from data_visualizer.profiler import AnalysisReport
from data_visualizer.settings import Settings

# Test dataset
df = pd.DataFrame({
    'numeric': [1, 2, 2, 3, 100],  # 100 is an outlier
    'categorical': ['A', 'B', 'A', 'B', 'C']
})

# Configure settings
settings = Settings(outlier_method='iqr', outlier_threshold=1.5)

# Generate report
report = AnalysisReport(df, settings=settings)
report.to_html('test_outliers.html')

# Check results
results = report.analyse()
print(results['variables']['numeric']['alerts'])  # Should include Outliers alert
