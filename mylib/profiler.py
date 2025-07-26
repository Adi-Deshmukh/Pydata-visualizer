import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AnalysisReport:
    
    
    def __init__(self,data):
        self.data = data

    def analyse(self):
        num_rows = self.data.shape[0] 
        num_columns = self.data.shape[1] 
        num_duplicates = self.data.duplicated().sum()
        
        overview_stats = {
        'num_Row': num_rows,
        'num_Columns': num_columns,
        'duplicated_rows': num_duplicates
        }
        
        return overview_stats