"""
Pydata-visualizer: A Python library for Exploratory Data Analysis and Profiling.
"""

__version__ = "1.0.0"

from .profiler import AnalysisReport, Settings
from .report import generate_html_report

__all__ = ['AnalysisReport', 'Settings', 'generate_html_report', '__version__']
