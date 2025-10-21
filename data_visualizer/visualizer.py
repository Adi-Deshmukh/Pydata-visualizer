import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64
import warnings
from typing import List, Optional, Union, Dict
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go
import json
from .settings import Settings

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Verdana']

def get_plot_as_base64(column_data: pd.Series, column_name: str, settings: "Settings" , outliers: Optional[List] = None, word_frequencies: Optional[dict] = None) -> Dict[str, Union[str, dict]]:
    
    if settings.use_plotly:
        if pd.api.types.is_numeric_dtype(column_data):
            # Numeric: Histogram with outliers
            fig = px.histogram(
                x=column_data.dropna(), nbins=20, title=f'Distribution of {column_name}',
                color_discrete_sequence=['#17a2b8']
            )
            if outliers:
                outlier_series = pd.Series(outliers)
                fig.add_trace(
                    go.Histogram(
                        x=outlier_series, nbinsx=20, name='Outliers',
                        marker_color='#dc3545', opacity=0.5
                    )
                )
            return {'type': 'plotly', 'data': json.loads(fig.to_json())}
        elif word_frequencies:
            # String: Word cloud as scatter (Plotly lacks native word clouds)
            words = list(word_frequencies.keys())
            sizes = list(word_frequencies.values())
            max_size = max(sizes) if sizes else 1
            fig = go.Figure(data=[
                go.Scatter(
                    x=[i % 5 for i in range(len(words))],  # Simple grid layout
                    y=[i // 5 for i in range(len(words))],
                    text=words,
                    mode='text',
                    textfont=dict(size=[max(1, min(s * 30 / max_size, 30)) for s in sizes]),
                    marker=dict(color='#2ca02c')
                )
            ])
            fig.update_layout(
                title=f'Word Cloud for {column_name}',
                showlegend=False, xaxis=dict(visible=False), yaxis=dict(visible=False)
            )
            return {'type': 'plotly', 'data': json.loads(fig.to_json())}
        else:
            # Categorical: Bar plot
            top_10 = column_data.value_counts().nlargest(10)
            fig = px.bar(
                x=top_10.index.astype(str), y=top_10.values,
                title=f'Top 10 Values for {column_name}',
                color_discrete_sequence=['#2ca02c']
            )
            fig.update_layout(xaxis_tickangle=45)
            return {'type': 'plotly', 'data': json.loads(fig.to_json())}
    else:
        # Seaborn logic
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
            plt.figure(figsize=(6, 4))
            plt.style.use('seaborn-v0_8-whitegrid')

            if pd.api.types.is_numeric_dtype(column_data):
                if outliers is not None:
                    inliers = column_data[~column_data.isin(outliers)]
                    sns.histplot(inliers, kde=True, bins=20, color="#17a2b8", label='Inliers')
                    if outliers:
                        sns.histplot(outliers, kde=False, bins=20, color="#dc3545", alpha=0.5, label='Outliers')
                    plt.legend()
                else:
                    sns.histplot(column_data, kde=True, bins=20, color="#17a2b8")
                plt.title(f'Distribution of {column_name}')
            elif word_frequencies is not None and word_frequencies:
                wordcloud = WordCloud(width=400, height=200, background_color='white', colormap='viridis').generate_from_frequencies(word_frequencies)
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                plt.title(f'Word Cloud for {column_name}')
            else:
                top_10 = column_data.value_counts().nlargest(10)
                clean_labels = [str(label).replace('$', '\\$').replace('_', '\\_') for label in top_10.index]
                sns.barplot(x=clean_labels, y=top_10.values, palette="viridis")
                plt.title(f'Top 10 Values for {column_name}')
                plt.xticks(rotation=45, ha='right')

            plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight')
            plt.close()
            data = base64.b64encode(buf.getbuffer()).decode('ascii')
            return {'type': 'base64', 'data': f"data:image/png;base64,{data}"}