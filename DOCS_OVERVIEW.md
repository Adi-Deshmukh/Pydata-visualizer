# Pydata-visualizer Documentation Overview

This repository contains comprehensive documentation for the Pydata-visualizer Python library for data analysis and profiling.

## Documentation Files

1. **[README.md](README.md)**: Main project documentation with overview, features, and basic usage.

2. **[DOCUMENTATION.md](DOCUMENTATION.md)**: Comprehensive technical documentation covering all components of the library.

3. **[USER_GUIDE.md](USER_GUIDE.md)**: Step-by-step guide for using the library, suitable for beginners.

4. **[INSTALLATION.md](INSTALLATION.md)**: Detailed installation instructions for various environments.

5. **[EXAMPLES.md](EXAMPLES.md)**: Practical examples showing how to use the library in different scenarios.

6. **[PYPI_DESCRIPTION.md](PYPI_DESCRIPTION.md)**: Description file formatted for PyPI listing.

## Quick Start

```python
import pandas as pd
from data_visualizer.profiler import AnalysisReport

# Load your dataset
df = pd.read_csv("your_dataset.csv")

# Create a report with default settings
report = AnalysisReport(df)
report.to_html("report.html")
```

## Documentation Structure

- **README.md**: Project overview, basic usage, and key features
- **DOCUMENTATION.md**: In-depth technical documentation on all aspects of the library
- **USER_GUIDE.md**: Practical guide for new users with step-by-step instructions
- **INSTALLATION.md**: Installation methods for different environments
- **EXAMPLES.md**: Code examples demonstrating common use cases
- **PYPI_DESCRIPTION.md**: Concise package description for PyPI

## Additional Resources

- GitHub Repository: [https://github.com/Adi-Deshmukh/Data_Profiler](https://github.com/Adi-Deshmukh/Data_Profiler)
- Issue Tracker: [https://github.com/Adi-Deshmukh/Data_Profiler/issues](https://github.com/Adi-Deshmukh/Data_Profiler/issues)
- PyPI Package: [https://pypi.org/project/pydata-visualizer/](https://pypi.org/project/pydata-visualizer/)

## Contributing

Contributions to the documentation are welcome! Please feel free to submit pull requests to improve any of these documents.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
