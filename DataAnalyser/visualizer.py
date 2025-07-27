import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64


#for univariate plots 
def get_plot_as_base64(column_data,column_name): 
    plt.figure(figsize=(8,6))
    if pd.api.types.is_numeric_dtype(column_data):
        sns.histplot(column_data)
        plt.title(column_name)
        plt.xticks(rotation=90,fontsize=10)
        
    else:
        sns.countplot(column_data)
        plt.title(column_name)
        plt.xticks(rotation=90,fontsize=10)
        
        

    #creates a in memory buffer file to store the plot image 
    buf = io.BytesIO()

    plt.tight_layout()
    plt.savefig(buf, format='png', bbox_inches = 'tight')
    
    plt.close()
    
    # this gets the buffer image and encodes it into base64 format used to embed in HTML files
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    
    return f"data:image/png;base64,{data}" # It is used to decode and render the image





