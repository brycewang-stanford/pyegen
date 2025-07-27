# ⚠️ This Repository Has Been Archived

This repository has been **archived** and is no longer maintained. 

All functionality from `pyegen` has been integrated into the unified **Py-Stata-Commands** package.

## 🔗 New Repository

Please use the new unified repository:
**https://github.com/brycewang-stanford/Py-Stata-Commands**

## 🚀 New Installation

```bash
pip install py-stata-commands
```

## 📖 New Usage

```python
from py_stata_commands import egen

# Same functionality, new location
df['rank_var'] = egen.rank(df['income'])
df['row_mean'] = egen.rowmean(df, ['var1', 'var2', 'var3'])
```

## 📚 Benefits of the New Package

- **Unified installation**: All Stata-equivalent commands in one package
- **Consistent API**: Familiar syntax across all modules
- **Better maintenance**: Single repository for all related functionality
- **Comprehensive documentation**: Complete examples and guides

---

**Migration**: Replace `import pyegen` with `from py_stata_commands import egen`