---

# PyEgen

[![PyPI version](https://badge.fury.io/py/pyegen.svg)](https://badge.fury.io/py/pyegen)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**⚠️ MIGRATION NOTICE**: This package has been integrated into the unified **Py-Stata-Commands** package.

## 🔄 Migration Instructions

**Old:**
```bash
pip install pyegen
```
```python
import pyegen as egen
df['rank_var'] = egen.rank(df['income'])
```

**New:**
```bash
pip install py-stata-commands
```
```python
from py_stata_commands import egen
df['rank_var'] = egen.rank(df['income'])
```

## 🎯 Why the Change?

The new unified package provides:
- **Single installation** for all Stata-equivalent commands (tabulate, egen, reghdfe, winsor2)
- **Consistent API** across all modules
- **Better documentation** and examples
- **Easier maintenance** and updates

## 📖 New Documentation

Visit the new repository for complete documentation:
**https://github.com/brycewang-stanford/Py-Stata-Commands**

---

*This repository is archived and will not receive further updates. Please migrate to the new package.*
