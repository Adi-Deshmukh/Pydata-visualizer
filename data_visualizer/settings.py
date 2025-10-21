# data_visualizer/settings.py
from pydantic import BaseModel, Field

class Settings(BaseModel):
    """
    Configuration settings for AnalysisReport.
    """
    minimal: bool = False
    top_n_values: int = Field(default=10, ge=1)
    skewness_threshold: float = Field(default=1.0, ge=0.0)
    outlier_method: str = Field(default='iqr', pattern='^(iqr|zscore)$')
    outlier_threshold: float = Field(default=1.5, ge=0.0)
    duplicate_threshold: float = Field(default=5.0, ge=0.0)  # % of rows duplicated to trigger alert
    text_analysis: bool = True  # Enable/disable text analysis
    use_plotly: bool = False  # Toggle Plotly vs. seaborn plots
    include_plots: bool = True  # Toggle plots/visualizations
    include_correlations : bool = True  # Toggle correlation analysis
    include_correlations_plots: bool = True  # Toggle correlation analysis/heatmaps
    include_correlations_json: bool = False  # Toggle correlation JSON data
    include_alerts: bool = True  # Toggle alerts (column and dataset-level)
    include_sample_data: bool = True  # Toggle head/tail samples
    include_overview: bool = True  # Toggle overview stats (core, but customizable)
    

    class Config:
        str_strip_whitespace = True