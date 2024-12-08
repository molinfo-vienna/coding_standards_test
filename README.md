# Python Project CI/CD Setup Guide

## Table of Contents
- [What is CI/CD?](#what-is-cicd)
- [Tools Overview](#tools-overview)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Code Quality Tools](#code-quality-tools)
- [Testing](#testing)
- [Package Configuration](#package-configuration)
- [Documentation Standards](#documentation-standards)

## What is CI/CD?

Continuous Integration/Continuous Deployment (CI/CD) is a software development approach that enables:

- **Continuous Integration (CI)**: Automatically integrating code changes from multiple contributors into a single software project. It's a coding philosophy and set of practices that drive development teams to frequently implement small code changes and check them in to version control repositories.

- **Continuous Deployment (CD)**: Automatically deploying all code changes to a testing and/or production environment after the build stage.

Benefits:
- Early bug detection
- Reduced manual errors
- Consistent test process
- Automatic build and deployment
- Continuous feedback

## Tools Overview

The minimum requirements setup uses several tools to ensure code quality and consistency:

### Code Formatters
- **Black**: Automatic code formatter
  - Installation: `pip install black`
  - Usage: `black .`
  - Purpose: Ensures consistent code style

- **isort**: Import statement organizer
  - Installation: `pip install isort`
  - Usage: `isort .`
  - Purpose: Organizes and formats import statements

### Code Quality
- **Pylint**: Static code analyzer
  - Installation: `pip install pylint`
  - Usage: `pylint your_package_name`
  - Purpose: Checks for errors and coding standards

- **pydocstyle**: Docstring checker
  - Installation: `pip install pydocstyle`
  - Usage: `pydocstyle your_package_name`
  - Purpose: Ensures documentation standards

### Testing
- **pytest**: Testing framework
  - Installation: `pip install pytest pytest-cov`
  - Usage: `pytest --cov=src`
  - Purpose: Runs tests and measures code coverage

## GitHub Actions Workflow

Our workflow file (`.github/workflows/python-package.yml`) handles:
- Multi-OS testing (Windows, macOS, Linux)
- Multiple Python versions
- Code quality checks
- Test execution
- Package building

For detailed information about the workflow file, see [Github Actions Workflow Explanation](#github-actions-workflow-explanation) below.

## Code Quality Tools

### Example Changes

#### Black Formatting
```python
# Before Black
x=[1,2,
3,4]

# After Black
x = [1, 2, 3, 4]
```

#### isort Import Sorting
```python
# Before isort
import sys
import os
from typing import List
import pandas

# After isort
import os
import sys
from typing import List

import pandas
```

## Documentation Standards

### Docstring Example
```python
def process_data(
    input_data: pd.DataFrame,
    threshold: float = 0.5,
    columns: Optional[List[str]] = None
) -> Tuple[pd.DataFrame, Dict[str, float]]:
    """Process input data and calculate statistical metrics.

    This function takes a pandas DataFrame, applies filtering based on the
    threshold value, and calculates various statistical metrics for specified
    columns.

    Args:
        input_data (pd.DataFrame): Input data to process.
            Must contain numeric columns.
        threshold (float, optional): Filtering threshold value.
            Values below this will be excluded. Defaults to 0.5.
        columns (List[str], optional): Specific columns to process.
            If None, all numeric columns will be processed.
            Defaults to None.

    Returns:
        Tuple[pd.DataFrame, Dict[str, float]]: A tuple containing:
            - processed_data: Filtered and processed DataFrame
            - metrics: Dictionary of calculated statistical metrics
                Keys are column names, values are computed metrics

    Raises:
        ValueError: If input_data is empty or contains no numeric columns
        TypeError: If threshold is not a float

    Examples:
        >>> data = pd.DataFrame({'A': [1, 2, 3], 'B': [0.1, 0.5, 0.8]})
        >>> processed, metrics = process_data(data, threshold=0.4)
        >>> print(metrics)
        {'A': 2.5, 'B': 0.65}

    Notes:
        - NaN values are automatically filtered out
        - Columns with all NaN values after filtering are dropped
    """
```
You can also use the Github Copilot for docstring generation


## Package Configuration

For detailed information about package configuration and setup, see [README_PACKAGE.md](README_PACKAGE.md).

## Running the Pipeline Locally

To run all checks locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run formatters
black .
isort .

# Run linters
pylint src tests
pydocstyle src

# Run tests
pytest tests/ --cov=src
```

## Contributing

Please ensure your pull requests adhere to the following guidelines:
- Run all formatters before committing
- Ensure all tests pass
- Add tests for new features
- Update documentation as needed

## License

This project is licensed under the MIT License - see the LICENSE file for details.