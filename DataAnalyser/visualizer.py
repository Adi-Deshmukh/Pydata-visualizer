import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64
import warnings # Import the warnings library

# --- FIX: Set a global font that supports a wider range of characters ---
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Verdana']
# --------------------------------------------------------------------

#for univariate plots 
def get_plot_as_base64(column_data, column_name) -> str:
    """
    Generates a plot for a given pandas Series, saves it to a memory buffer,
    and returns it as a Base64 encoded string for HTML embedding.
    """
    # --- FIX: Temporarily ignore font warnings during plot creation ---
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

        plt.figure(figsize=(8, 6))
        plt.style.use('seaborn-v0_8-whitegrid')

        if pd.api.types.is_numeric_dtype(column_data):
            sns.histplot(column_data, kde=True, bins=20, color="#17a2b8")
            plt.title(f'Distribution of {column_name}')
        else:
            top_10 = column_data.value_counts().nlargest(10)
            
            # --- FIX: Sanitize labels to escape special mathtext characters like '$' and '_' ---
            # This prevents matplotlib from crashing when it sees special characters.
            clean_labels = [
                str(label).replace('$', '\\$').replace('_', '\\_')
                for label in top_10.index
            ]
            
            sns.barplot(x=clean_labels, y=top_10.values, palette="viridis")
            plt.title(f'Top 10 Values for {column_name}')
            plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        
        # Save plot to a memory buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        plt.close()

    # Encode buffer to a base64 string
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    
    return f"data:image/png;base64,{data}"
