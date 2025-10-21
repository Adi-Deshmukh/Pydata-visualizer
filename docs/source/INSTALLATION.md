# Installation Guide for Pydata-visualizer

This guide provides detailed instructions for installing Pydata-visualizer in various environments.

## Requirements

- Python 3.8 or higher
- pip (Python package installer)

## Basic Installation

The simplest way to install Pydata-visualizer is using pip:

```bash
pip install pydata-visualizer
```

This will install the library and all its dependencies.

## Installation Options

### Install from PyPI with all extras

For a complete installation with all optional features:

```bash
pip install "pydata-visualizer[complete]"
```

### Install from GitHub

To install the latest development version:

```bash
pip install git+https://github.com/Adi-Deshmukh/Pydata-visualizer.git
```

### Local Development Installation

For development purposes, you can install the package in editable mode:

```bash
git clone https://github.com/Adi-Deshmukh/Pydata-visualizer.git
cd Pydata-visualizer
pip install -e .
```

## Environment-specific Instructions

### Conda Environment

```bash
# Create a new conda environment
conda create -n data-viz python=3.10
conda activate data-viz

# Install the package
pip install pydata-visualizer
```

### Virtual Environment (venv)

```bash
# Create a virtual environment
python -m venv data_viz_env
source data_viz_env/bin/activate  # On Windows: data_viz_env\Scripts\activate

# Install the package
pip install pydata-visualizer
```

### Jupyter Notebook

If you're using Jupyter Notebook, you can install the package and use it in your notebooks:

```bash
pip install pydata-visualizer

# Then in your notebook:
# import pandas as pd
# from data_visualizer.profiler import AnalysisReport
# ...
```

## Troubleshooting

### Missing Dependencies

If you encounter errors related to missing dependencies, try installing them explicitly:

```bash
pip install pandas matplotlib seaborn numpy scipy jinja2 visions pydantic colorama tqdm imagehash wordcloud plotly shapely
```

### Matplotlib Backend Issues

If you encounter issues with matplotlib visualizations, you may need to set a non-interactive backend:

```python
import matplotlib
matplotlib.use('Agg')  # Set before importing pyplot
```

### Installation in Restricted Environments

In environments with restricted permissions:

```bash
pip install --user pydata-visualizer
```

### Verifying Installation

You can verify that the installation was successful by running:

```python
import data_visualizer
print(data_visualizer.__version__)  # Should print the installed version
```

## Dependencies

The following dependencies will be automatically installed:

- imagehash
- Jinja2
- matplotlib
- numpy
- pandas
- pydantic
- scipy
- seaborn
- shapely
- visions
- tqdm
- colorama
- wordcloud
- plotly

## Upgrading

To upgrade to the latest version:

```bash
pip install --upgrade pydata-visualizer
```

## Uninstallation

To remove the package:

```bash
pip uninstall pydata-visualizer
```
