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

    class Config:
        str_strip_whitespace = True