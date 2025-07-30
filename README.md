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
import pyegen as egen

# Create sample data
df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'value': [10, 20, 30, 40, 50, 60]
})

# Generate ranks
df['rank'] = egen.rank(df['value'])

# Calculate group means
df['group_mean'] = egen.mean(df['value'], by=df['group'])

# Row-wise operations
df['row_sum'] = egen.rowtotal(df, ['value'])
```

## Available Functions

PyEgen supports **40+ functions** covering all major Stata egen capabilities:

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

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- **[PyStataR](https://github.com/brycewang-stanford/PyStataR)** - Unified Stata-equivalent commands and R functions (recommended for new projects)
- **[StatsPAI](https://github.com/brycewang-stanford/StatsPAI/)** - StatsPAI = Stats + Econometrics + ML + AI + LLMs