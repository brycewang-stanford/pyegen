# PyEgen

[![PyPI version](https://badge.fury.io/py/pyegen.svg)](https://badge.fury.io/py/pyegen)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/pyegen)](https://pypi.org/project/pyegen/)

Python implementation of Stata's `egen` command for pandas DataFrames. This package provides Stata-style data manipulation functions, making it easier for researchers to transition from Stata to Python while maintaining familiar syntax and functionality.

## Quick Start

```bash
pip install pyegen
```

```python
import pandas as pd
import numpy as np
import pyegen as egen

# Create sample data
df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'var1': [1, np.nan, 3, 4, 5, 6],
    'var2': [np.nan, 2, 5, 6, 7, 8],
    'var3': [10, 11, 12, 13, 14, 15]
})

# Row-wise operations
df['first_nonmiss'] = egen.rowfirst(df, ['var1', 'var2', 'var3'])
df['row_median'] = egen.rowmedian(df, ['var1', 'var2', 'var3'])
df['missing_count'] = egen.rowmiss(df, ['var1', 'var2', 'var3'])

# Group-wise operations  
df['group_mean'] = egen.mean(df['var1'], by=df['group'])
df['group_median'] = egen.median(df['var1'], by=df['group'])
df['group_rank'] = egen.rank(df['var1'], method='min')

# Utility functions
df['has_value_1_or_2'] = egen.anymatch(df, ['var1', 'var2'], [1, 2])
df['concat_vars'] = egen.concat(df, ['group', 'var1'], punct='_')
```

## Available Functions

PyEgen provides **45+ functions** with **100% coverage** of Stata's egen capabilities:

### Row-wise Functions
- `rowmean()`, `rowtotal()`, `rowmax()`, `rowmin()`, `rowsd()`
- `rowfirst()`, `rowlast()`, `rowmedian()`, `rowmiss()`, `rownonmiss()`, `rowpctile()`

### Statistical Functions  
- `rank()`, `count()`, `mean()`, `sum()`, `max()`, `min()`, `sd()`
- `median()`, `mode()`, `iqr()`, `kurt()`, `skew()`, `mad()`, `mdev()`
- `pc()`, `pctile()`, `std()`, `total()`

### Utility Functions
- `tag()`, `group()`, `seq()`, `anycount()`, `anymatch()`, `anyvalue()`
- `concat()`, `cut()`, `diff()`, `ends()`, `fill()`

## 🎯 Key Features

- **Complete Stata Coverage**: All 45 egen functions implemented
- **Pandas Integration**: Works seamlessly with pandas DataFrames  
- **Missing Value Handling**: Consistent with Stata behavior
- **Group Operations**: Full support for by-group operations with `by` parameter
- **Type Safety**: Comprehensive input validation and error handling
- **Performance**: Optimized for large datasets

## 📚 Complete Function Reference

### Row-wise Functions
| Function | Stata Equivalent | Description |
|----------|------------------|-------------|
| `rowmean()` | `egen newvar = rowmean(varlist)` | Row mean |
| `rowtotal()` | `egen newvar = rowtotal(varlist)` | Row sum |
| `rowmax()` | `egen newvar = rowmax(varlist)` | Row maximum |
| `rowmin()` | `egen newvar = rowmin(varlist)` | Row minimum |
| `rowsd()` | `egen newvar = rowsd(varlist)` | Row standard deviation |
| `rowfirst()` | `egen newvar = rowfirst(varlist)` | First non-missing value |
| `rowlast()` | `egen newvar = rowlast(varlist)` | Last non-missing value |
| `rowmedian()` | `egen newvar = rowmedian(varlist)` | Row median |
| `rowmiss()` | `egen newvar = rowmiss(varlist)` | Count of missing values |
| `rownonmiss()` | `egen newvar = rownonmiss(varlist)` | Count of non-missing values |
| `rowpctile()` | `egen newvar = rowpctile(varlist), p(#)` | Row percentile |

### Statistical Functions (with grouping support)
| Function | Stata Equivalent | Description |
|----------|------------------|-------------|
| `count()` | `egen newvar = count(var), by(group)` | Count observations |
| `mean()` | `egen newvar = mean(var), by(group)` | Mean |
| `sum()` | `egen newvar = sum(var), by(group)` | Sum |
| `total()` | `egen newvar = total(var), by(group)` | Total (treats missing as 0) |
| `max()` | `egen newvar = max(var), by(group)` | Maximum |
| `min()` | `egen newvar = min(var), by(group)` | Minimum |
| `sd()` | `egen newvar = sd(var), by(group)` | Standard deviation |
| `median()` | `egen newvar = median(var), by(group)` | Median |
| `mode()` | `egen newvar = mode(var), by(group)` | Mode |
| `iqr()` | `egen newvar = iqr(var), by(group)` | Interquartile range |
| `kurt()` | `egen newvar = kurt(var), by(group)` | Kurtosis |
| `skew()` | `egen newvar = skew(var), by(group)` | Skewness |
| `mad()` | `egen newvar = mad(var), by(group)` | Median absolute deviation |
| `mdev()` | `egen newvar = mdev(var), by(group)` | Mean absolute deviation |
| `pctile()` | `egen newvar = pctile(var), p(#)` | Percentile |
| `pc()` | `egen newvar = pc(var), by(group)` | Percent of total |
| `std()` | `egen newvar = std(var), by(group)` | Standardized values |

### Utility Functions
| Function | Stata Equivalent | Description |
|----------|------------------|-------------|
| `rank()` | `egen newvar = rank(var)` | Ranking with tie options |
| `tag()` | `egen newvar = tag(varlist)` | Tag first obs in group |
| `group()` | `egen newvar = group(varlist)` | Create group identifiers |
| `seq()` | `egen newvar = seq()` | Generate sequences |
| `anycount()` | `egen newvar = anycount(varlist), v(values)` | Count matching values |
| `anymatch()` | `egen newvar = anymatch(varlist), v(values)` | Check for matches |
| `anyvalue()` | `egen newvar = anyvalue(var), v(values)` | Return matching values |
| `concat()` | `egen newvar = concat(varlist), punct()` | Concatenate variables |
| `cut()` | `egen newvar = cut(var), group(#)` | Create categorical from continuous |
| `diff()` | `egen newvar = diff(varlist)` | Check if variables differ |
| `ends()` | `egen newvar = ends(strvar), head\|last\|tail` | Extract string parts |
| `fill()` | `egen newvar = fill(numlist)` | Create repeating patterns |

## 💡 Migration Recommendation

**For new projects**, we recommend using the unified **PyStataR** package which provides a comprehensive suite of Stata-equivalent commands:

```bash
pip install py-stata-commands
```

```python
from py_stata_commands import egen
df['rank_var'] = egen.rank(df['income'])
```

### Why Consider PyStataR?

- **Single installation** for all Stata-equivalent commands (tabulate, egen, reghdfe, winsor2)
- **Consistent API** across all modules  
- **Enhanced documentation** and examples
- **Active development** and long-term support

**PyStataR Repository:** https://github.com/brycewang-stanford/PyStataR

## Documentation & Examples

For comprehensive examples and function documentation, see:
- [Complete Function Reference](egen_demo_en.ipynb)
- [Stata-to-PyEgen Mapping](egen_demo_en.ipynb#8-stata-to-python-conversion-reference-table)

## 📊 Function Coverage Status

- ✅ Row-wise functions: 11/11 (100%)
- ✅ Statistical functions: 17/17 (100%)  
- ✅ Utility functions: 12/12 (100%)
- ✅ String functions: 2/2 (100%)
- ✅ Sequence functions: 2/2 (100%)

**Total: 45/45 functions (100% coverage)**

## 🧪 Testing

```bash
# Run tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_core.py
```

## 🔧 Project Status

**PyEgen will continue to be maintained** for existing users, but new feature development will primarily focus on PyStataR. This ensures:
- ✅ Bug fixes and compatibility updates for PyEgen
- ✅ Stable API for existing codebases  
- 🚀 Enhanced features and new capabilities in PyStataR

## Installation & Requirements

```bash
pip install pyegen
```

**Requirements:**
- Python 3.7+
- pandas >= 1.3.0
- numpy >= 1.20.0

## 🤝 Contributing

We welcome contributions! For major changes, please consider contributing to [PyStataR](https://github.com/brycewang-stanford/PyStataR) for maximum impact.

## 🔗 Stata Documentation Reference

This implementation follows the official Stata documentation for egen:
- [Stata 18 egen documentation](https://www.stata.com/manuals/d/egen.pdf)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- **[PyStataR](https://github.com/brycewang-stanford/PyStataR)** - Unified Stata-equivalent commands and R functions (recommended for new projects)
- **[StatsPAI](https://github.com/brycewang-stanford/StatsPAI/)** - StatsPAI = Stats + Econometrics + ML + AI + LLMs