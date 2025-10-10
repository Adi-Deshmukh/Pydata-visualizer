import io
import math
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from itertools import combinations
import matplotlib.pyplot as plt
import seaborn as sns
import base64


def calculate_correlations(data):
    columns = data.columns

    # Segregating Data Types 
    categorical_df = data.select_dtypes(include='object')
    numerical_df = data.select_dtypes(include='number')

    pearson_corr= numerical_df.corr(method='pearson') # Linear relations and scatter plots (numerical df)
    spearman_corr= numerical_df.corr(method='spearman') # Checks General Trend (numerical df)

    categorical_columns = categorical_df.columns
    
    cramers_v_matrix= pd.DataFrame(index=categorical_columns,
                            columns=categorical_columns)  # To store values (rows & columns == Variables) 

    for col1, col2 in combinations(categorical_columns, 2):
        cramers_v = _cramers_v(categorical_df[col1], categorical_df[col2])
        # Created a Correlation Matrix for Cramér's V results to solve the return problem
        cramers_v_matrix.loc[col1, col2] = cramers_v
        cramers_v_matrix.loc[col2, col1] = cramers_v  # To make the result symmetrical
    
    # Fill diagonal with 1s after processing all pairs
    if len(categorical_columns) > 0:
        np.fill_diagonal(cramers_v_matrix.values, 1.0)
        cramers_v_matrix = cramers_v_matrix.astype(float)
    
    correlations = {
        "pearson": pearson_corr,
        "spearman": spearman_corr,
        "cramers_v": cramers_v_matrix
    }
    
    return correlations

    

def _cramers_v(c_1_series, c_2_series):

    contingency_table = pd.crosstab(c_1_series, c_2_series) # Created a contingency table for cross tabulation

    chi2 = chi2_contingency(contingency_table)[0] # Chi-squared statistic
    n = contingency_table.values.sum() # Total number of observations
    min_dim = min(contingency_table.shape) # Minimum dimension of the contingency table
    
    try:
        v = math.sqrt(chi2 / (n * (min_dim - 1))) # Cramér's V
    except ZeroDivisionError:
        # If a ZeroDivisionError occurs, it means one column was constant.
        # In this case, the correlation is 0.
        v = 0.0
    
    return v

# Heatmap Generation
def generate_correlation_heatmap(correlation_matrix):
    """
    Generates a heatmap for the correlation matrix and returns it as a Base64 encoded string.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True, cbar_kws={"shrink": .8})
    plt.title("Correlation Heatmap")
    plt.tight_layout()

    # Save plot to a memory buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()

    # Encode buffer to a base64 string
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    
    return f"data:image/png;base64,{data}"




