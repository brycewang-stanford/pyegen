# PyEgen

[![PyPI version](https://badge.fury.io/py/pyegen.svg)](https://badge.fury.io/py/pyegen)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

🐍 **Python implementation of Stata's `egen` command**

PyEgen brings the power and convenience of Stata's `egen` (extended generate) command to Python pandas DataFrames. If you're a researcher transitioning from Stata to Python, this package will make your data manipulation tasks much more familiar and efficient.

##  Key Features

- **Familiar Syntax**: Stata-like syntax for data manipulation
- **Pandas Integration**: Seamless integration with pandas DataFrames  
- **High Performance**: Optimized implementations using pandas operations
- **Comprehensive**: Covers most commonly used `egen` functions
- **Easy to Use**: Simple, intuitive API

##  Installation

```bash
pip install pyegen
```

##  Quick Start

```python
import pandas as pd
import pyegen as egen

# Create sample data
df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'value1': [10, 20, 30, 40, 50, 60],
    'value2': [1, 2, 3, 4, 5, 6],
    'value3': [100, 200, 300, 400, 500, 600]
})

# Stata: egen newvar = rank(value1)
df['rank_val'] = egen.rank(df['value1'])

# Stata: egen newvar = rowmean(value1 value2 value3)
df['row_mean'] = egen.rowmean(df, ['value1', 'value2', 'value3'])

# Stata: egen newvar = rowtotal(value1 value2 value3)
df['row_total'] = egen.rowtotal(df, ['value1', 'value2', 'value3'])

# Stata: egen newvar = tag(group)
df['tag'] = egen.tag(df, ['group'])

# Stata: egen newvar = count(value1), by(group)
df['count_by_group'] = egen.count(df['value1'], by=df['group'])
```

##  Available Functions

### Basic Functions
- **`rank(series, method='average')`** - Rank values (like Stata's `egen rank`)
- **`rowmean(df, columns)`** - Row-wise mean across specified columns
- **`rowtotal(df, columns)`** - Row-wise sum across specified columns
- **`rowmax(df, columns)`** - Row-wise maximum across specified columns
- **`rowmin(df, columns)`** - Row-wise minimum across specified columns
- **`rowcount(df, columns)`** - Count non-missing values across columns
- **`rowsd(df, columns)`** - Row-wise standard deviation

### Grouping Functions
- **`tag(df, columns)`** - Tag first occurrence in each group
- **`count(series, by=None)`** - Count observations (optionally by group)
- **`mean(series, by=None)`** - Group means
- **`sum(series, by=None)`** - Group sums
- **`max(series, by=None)`** - Group maxima
- **`min(series, by=None)`** - Group minima
- **`sd(series, by=None)`** - Group standard deviations

### Advanced Functions
- **`seq()`** - Generate sequence numbers
- **`group(df, columns)`** - Create group identifiers
- **`pc(series, by=None)`** - Calculate percentiles
- **`iqr(series, by=None)`** - Interquartile range

## 💡 Detailed Examples

### Working with Missing Values
```python
import numpy as np

# Data with missing values
df = pd.DataFrame({
    'var1': [1, 2, np.nan, 4, 5],
    'var2': [10, np.nan, 30, 40, 50],
    'var3': [100, 200, 300, np.nan, 500]
})

# Row statistics excluding missing values
df['mean_nonmissing'] = egen.rowmean(df, ['var1', 'var2', 'var3'])
df['count_nonmissing'] = egen.rowcount(df, ['var1', 'var2', 'var3'])
```

### Group Operations
```python
# Sample data with groups
df = pd.DataFrame({
    'country': ['USA', 'USA', 'CHN', 'CHN', 'DEU', 'DEU'],
    'year': [2020, 2021, 2020, 2021, 2020, 2021],
    'gdp': [21.43, 22.32, 14.72, 17.73, 3.84, 4.26],
    'population': [331, 332, 1439, 1412, 83, 83]
})

# Group-wise operations
df['mean_gdp_by_country'] = egen.mean(df['gdp'], by=df['country'])
df['country_tag'] = egen.tag(df, ['country'])
df['obs_per_country'] = egen.count(df['gdp'], by=df['country'])
```

### Ranking and Percentiles
```python
# Ranking
df['gdp_rank'] = egen.rank(df['gdp'])  # Overall ranking
df['gdp_rank_by_year'] = egen.rank(df['gdp'], by=df['year'])  # Ranking within year

# Percentiles
df['gdp_percentile'] = egen.pc(df['gdp'])
```

##  Stata to Python Translation Guide

| Stata Command | PyEgen Equivalent |
|---------------|-------------------|
| `egen newvar = rank(var)` | `df['newvar'] = egen.rank(df['var'])` |
| `egen newvar = rowmean(var1-var3)` | `df['newvar'] = egen.rowmean(df, ['var1', 'var2', 'var3'])` |
| `egen newvar = rowtotal(var1-var3)` | `df['newvar'] = egen.rowtotal(df, ['var1', 'var2', 'var3'])` |
| `egen newvar = tag(group)` | `df['newvar'] = egen.tag(df, ['group'])` |
| `egen newvar = count(var), by(group)` | `df['newvar'] = egen.count(df['var'], by=df['group'])` |
| `egen newvar = mean(var), by(group)` | `df['newvar'] = egen.mean(df['var'], by=df['group'])` |

## 🚀 Roadmap & Future Features

PyEgen is actively developed with plans to expand functionality in upcoming versions. Here's what's on the horizon:

### 📋 Version 0.2.0 (Next Release)
**Enhanced egen Functions**
- **`seq()`** - Generate sequence numbers (1, 2, 3, ...) and custom sequences
- **`cut()`** - Create categorical variables from continuous data with custom breakpoints
- **`recode()`** - Recode values based on conditions (like Stata's recode command)
- **`std()`** - Standardize variables (z-scores) with optional group-wise standardization
- **`pctile()`** - Calculate specific percentiles (25th, 75th, 90th, etc.)

**Performance & Usability**
- **Improved error handling** with more informative error messages
- **Performance optimizations** for large datasets (10M+ rows)
- **Better missing value handling** with flexible options
- **Enhanced documentation** with more real-world examples

### 📈 Version 0.3.0 (Medium-term)
**Advanced Data Operations**
- **`bysort` syntax sugar** - Simplified group operations with Stata-like syntax
- **`diff()` and `lag()`** - Time series operations for panel data
- **`egen modes()`** - Find modal values within groups
- **`egen total()` variations** - Cumulative sums, running totals
- **Data validation functions** - Automatic data quality checks

**Integration Features**
- **Categorical data support** - Enhanced handling of pandas categorical types
- **DateTime operations** - Date-based grouping and time series functions
- **Memory optimization** - Efficient processing of large datasets
- **Export utilities** - Direct integration with popular data formats

### 🔮 Version 1.0.0 (Long-term Vision)
**Comprehensive Stata Migration**
- **`tabulate` equivalents** - Cross-tabulation and frequency tables
- **`margins` functionality** - Marginal effects and predictions
- **`collapse` operations** - Data aggregation with multiple statistics
- **Label handling** - Variable and value labels (Stata-style metadata)

**Ecosystem Integration**
- **Jupyter notebook magic commands** - `%%pyegen` cell magic for easier usage
- **Integration with popular packages** - scikit-learn, statsmodels, plotly
- **Cloud computing support** - Optimizations for Dask and Ray
- **Educational resources** - Interactive tutorials and case studies

### 💡 Community-Driven Features

We're always looking for community input! Planned features based on user feedback:

- **Custom function plugins** - Allow users to contribute domain-specific functions
- **Performance benchmarking** - Tools to compare PyEgen vs. native pandas performance
- **Migration assistant** - Tools to semi-automatically convert Stata .do files
- **Academic paper examples** - Replications of common econometric analyses

### 🎯 Why These Features Matter

**For Researchers**: Smoother transition from Stata to Python with familiar syntax
**For Data Scientists**: Powerful data manipulation without learning new paradigms  
**For Educators**: Teaching data analysis with consistent, intuitive functions
**For Performance**: Optimized operations that scale from small datasets to big data

Want to see a specific feature prioritized? **Open an issue** or start a **discussion** on our GitHub repository!

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
git clone https://github.com/brycewang-stanford/pyegen.git
cd pyegen
pip install -e ".[dev]"
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by Stata's `egen` command
- Built on the excellent pandas library
- Thanks to the open-source community for feedback and contributions

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/brycewang-stanford/pyegen/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/brycewang-stanford/pyegen/discussions)
- 📧 **Email**: brycew6m@stanford.edu

---

⭐ **If this package helps your research, please consider starring the repository!**
