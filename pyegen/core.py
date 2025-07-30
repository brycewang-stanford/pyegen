"""
Core implementation of PyEgen functions.

This module contains the main implementations of Stata's egen functions
adapted for pandas DataFrames.
"""

import numpy as np
import pandas as pd
from typing import Union, List, Optional, Any, Tuple
import warnings


def _validate_dataframe(df: pd.DataFrame) -> None:
    """Validate that input is a pandas DataFrame."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")


def _validate_series(series: pd.Series) -> None:
    """Validate that input is a pandas Series."""
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")


def _validate_columns(df: pd.DataFrame, columns: List[str]) -> None:
    """Validate that specified columns exist in DataFrame."""
    missing_cols = set(columns) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Columns not found in DataFrame: {missing_cols}")


# ============================================================================
# Basic Functions
# ============================================================================

def rank(series: pd.Series, method: str = 'average', ascending: bool = True) -> pd.Series:
    """
    Generate ranks for a pandas Series.
    
    Equivalent to Stata's: egen newvar = rank(var)
    
    Parameters:
    -----------
    series : pd.Series
        Input series to rank
    method : str, default 'average'
        How to rank tied values ('average', 'min', 'max', 'first', 'dense')
    ascending : bool, default True
        Whether to rank in ascending order
        
    Returns:
    --------
    pd.Series
        Ranked values
        
    Examples:
    ---------
    >>> import pandas as pd
    >>> import pyegen as egen
    >>> df = pd.DataFrame({'var': [10, 20, 30, 20, 40]})
    >>> df['rank_var'] = egen.rank(df['var'])
    """
    _validate_series(series)
    return series.rank(method=method, ascending=ascending)


def rowmean(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Calculate row-wise mean across specified columns.
    
    Equivalent to Stata's: egen newvar = rowmean(var1-var3)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to calculate mean across
        
    Returns:
    --------
    pd.Series
        Row-wise means
        
    Examples:
    ---------
    >>> import pandas as pd
    >>> import pyegen as egen
    >>> df = pd.DataFrame({
    ...     'var1': [1, 2, 3],
    ...     'var2': [4, 5, 6],
    ...     'var3': [7, 8, 9]
    ... })
    >>> df['row_mean'] = egen.rowmean(df, ['var1', 'var2', 'var3'])
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    return df[columns].mean(axis=1)


def rowtotal(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Calculate row-wise sum across specified columns.
    
    Equivalent to Stata's: egen newvar = rowtotal(var1-var3)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to sum across
        
    Returns:
    --------
    pd.Series
        Row-wise sums
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    return df[columns].sum(axis=1)


def rowmax(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Calculate row-wise maximum across specified columns.
    
    Equivalent to Stata's: egen newvar = rowmax(var1-var3)
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    return df[columns].max(axis=1)


def rowmin(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Calculate row-wise minimum across specified columns.
    
    Equivalent to Stata's: egen newvar = rowmin(var1-var3)
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    return df[columns].min(axis=1)


def rowcount(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Count non-missing values across specified columns for each row.
    
    Equivalent to Stata's: egen newvar = rownonmiss(var1-var3)
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    return df[columns].count(axis=1)


def rowsd(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Calculate row-wise standard deviation across specified columns.
    
    Equivalent to Stata's: egen newvar = rowsd(var1-var3)
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    return df[columns].std(axis=1)


# ============================================================================
# Grouping Functions
# ============================================================================

def tag(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Tag the first occurrence in each group.
    
    Equivalent to Stata's: egen newvar = tag(group1 group2)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names that define groups
        
    Returns:
    --------
    pd.Series
        Binary series (1 for first occurrence, 0 otherwise)
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    
    # Create a copy to avoid modifying original
    temp_df = df[columns].copy()
    
    # Mark first occurrence of each combination
    is_first = ~temp_df.duplicated()
    
    return is_first.astype(int)


def count(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Count non-missing observations, optionally by group.
    
    Equivalent to Stata's: egen newvar = count(var) [, by(group)]
    
    Parameters:
    -----------
    series : pd.Series
        Series to count
    by : pd.Series, optional
        Grouping variable
        
    Returns:
    --------
    pd.Series
        Count of non-missing observations (by group if specified)
    """
    _validate_series(series)
    
    if by is None:
        # Overall count
        total_count = series.count()
        return pd.Series([total_count] * len(series), index=series.index)
    else:
        # Group-wise count
        _validate_series(by)
        return series.groupby(by).transform('count')


def mean(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate mean, optionally by group.
    
    Equivalent to Stata's: egen newvar = mean(var) [, by(group)]
    """
    _validate_series(series)
    
    if by is None:
        overall_mean = series.mean()
        return pd.Series([overall_mean] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform('mean')


def sum(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate sum, optionally by group.
    
    Equivalent to Stata's: egen newvar = sum(var) [, by(group)]
    """
    _validate_series(series)
    
    if by is None:
        overall_sum = series.sum()
        return pd.Series([overall_sum] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform('sum')


def max(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate maximum, optionally by group.
    
    Equivalent to Stata's: egen newvar = max(var) [, by(group)]
    """
    _validate_series(series)
    
    if by is None:
        overall_max = series.max()
        return pd.Series([overall_max] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform('max')


def min(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate minimum, optionally by group.
    
    Equivalent to Stata's: egen newvar = min(var) [, by(group)]
    """
    _validate_series(series)
    
    if by is None:
        overall_min = series.min()
        return pd.Series([overall_min] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform('min')


def sd(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate standard deviation, optionally by group.
    
    Equivalent to Stata's: egen newvar = sd(var) [, by(group)]
    """
    _validate_series(series)
    
    if by is None:
        overall_sd = series.std()
        return pd.Series([overall_sd] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform('std')


# ============================================================================
# Advanced Functions
# ============================================================================

def seq() -> None:
    """
    Generate sequence numbers.
    
    Note: This function will be implemented in a future version.
    For now, use: pd.Series(range(1, len(df) + 1))
    """
    raise NotImplementedError("seq() function will be implemented in a future version")


def group(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Create group identifiers.
    
    Equivalent to Stata's: egen newvar = group(var1 var2)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to group by
        
    Returns:
    --------
    pd.Series
        Group identifiers (integers starting from 1)
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    
    # Create group identifiers
    grouped = df[columns].drop_duplicates().reset_index(drop=True)
    grouped['_group_id'] = range(1, len(grouped) + 1)
    
    # Merge back to original data
    result = df[columns].merge(grouped, on=columns, how='left')
    
    return result['_group_id']


def pc(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate percentile ranks.
    
    Equivalent to Stata's: egen newvar = pc(var) [, by(group)]
    """
    _validate_series(series)
    
    if by is None:
        return series.rank(pct=True) * 100
    else:
        _validate_series(by)
        return series.groupby(by).rank(pct=True) * 100


def iqr(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate interquartile range.
    
    Equivalent to Stata's: egen newvar = iqr(var) [, by(group)]
    """
    _validate_series(series)
    
    def _iqr(x):
        return x.quantile(0.75) - x.quantile(0.25)
    
    if by is None:
        overall_iqr = _iqr(series)
        return pd.Series([overall_iqr] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform(_iqr)


# ============================================================================
# New Row-wise Functions
# ============================================================================

def rowfirst(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Get first non-missing value in each row.
    
    Equivalent to Stata's: egen newvar = rowfirst(var1-var3)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to examine
        
    Returns:
    --------
    pd.Series
        First non-missing value in each row
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    
    def get_first_nonmissing(row):
        for col in columns:
            val = row[col]
            if pd.notna(val):
                return val
        return np.nan
    
    return df[columns].apply(get_first_nonmissing, axis=1)


def rowlast(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Get last non-missing value in each row.
    
    Equivalent to Stata's: egen newvar = rowlast(var1-var3)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to examine
        
    Returns:
    --------
    pd.Series
        Last non-missing value in each row
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    
    def get_last_nonmissing(row):
        for col in reversed(columns):
            val = row[col]
            if pd.notna(val):
                return val
        return np.nan
    
    return df[columns].apply(get_last_nonmissing, axis=1)


def rowmedian(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Calculate row-wise median across specified columns.
    
    Equivalent to Stata's: egen newvar = rowmedian(var1-var3)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to calculate median across
        
    Returns:
    --------
    pd.Series
        Row-wise medians
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    return df[columns].median(axis=1)


def rowmiss(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Count missing values across specified columns for each row.
    
    Equivalent to Stata's: egen newvar = rowmiss(var1-var3)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to examine
        
    Returns:
    --------
    pd.Series
        Number of missing values in each row
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    return df[columns].isnull().sum(axis=1)


def rownonmiss(df: pd.DataFrame, columns: List[str], strok: bool = False) -> pd.Series:
    """
    Count non-missing values across specified columns for each row.
    
    Equivalent to Stata's: egen newvar = rownonmiss(var1-var3) [, strok]
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to examine
    strok : bool, default False
        Whether to allow string variables
        
    Returns:
    --------
    pd.Series
        Number of non-missing values in each row
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    
    if not strok:
        # Check if any columns are string type
        string_cols = [col for col in columns if df[col].dtype == 'object']
        if string_cols:
            warnings.warn(f"String columns found: {string_cols}. Use strok=True to include them.")
            # Filter out string columns
            columns = [col for col in columns if col not in string_cols]
    
    if not columns:
        return pd.Series([0] * len(df), index=df.index)
    
    return df[columns].count(axis=1)


def rowpctile(df: pd.DataFrame, columns: List[str], p: float = 50) -> pd.Series:
    """
    Calculate row-wise percentile across specified columns.
    
    Equivalent to Stata's: egen newvar = rowpctile(var1-var3), p(#)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to calculate percentile across
    p : float, default 50
        Percentile to calculate (0-100)
        
    Returns:
    --------
    pd.Series
        Row-wise percentiles
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    
    if not 0 <= p <= 100:
        raise ValueError("Percentile p must be between 0 and 100")
    
    return df[columns].quantile(p/100, axis=1)


# ============================================================================
# New Statistical Functions
# ============================================================================

def median(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate median, optionally by group.
    
    Equivalent to Stata's: egen newvar = median(var) [, by(group)]
    
    Parameters:
    -----------
    series : pd.Series
        Input series
    by : pd.Series, optional
        Grouping variable
        
    Returns:
    --------
    pd.Series
        Median values (by group if specified)
    """
    _validate_series(series)
    
    if by is None:
        overall_median = series.median()
        return pd.Series([overall_median] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform('median')


def mode(series: pd.Series, by: Optional[pd.Series] = None, 
         minmode: bool = False, maxmode: bool = False, 
         nummode: Optional[int] = None, missing: bool = False) -> pd.Series:
    """
    Calculate mode, optionally by group.
    
    Equivalent to Stata's: egen newvar = mode(var) [, by(group) minmode maxmode nummode(#) missing]
    
    Parameters:
    -----------
    series : pd.Series
        Input series
    by : pd.Series, optional
        Grouping variable
    minmode : bool, default False
        Return the lowest mode if multiple modes exist
    maxmode : bool, default False
        Return the highest mode if multiple modes exist
    nummode : int, optional
        Return the nth mode (1-indexed)
    missing : bool, default False
        Include missing values in mode calculation
        
    Returns:
    --------
    pd.Series
        Mode values (by group if specified)
    """
    _validate_series(series)
    
    def _mode(x):
        if not missing:
            x = x.dropna()
        if len(x) == 0:
            return np.nan
        
        mode_values = x.mode()
        if len(mode_values) == 0:
            return np.nan
        elif len(mode_values) == 1:
            return mode_values.iloc[0]
        else:
            # Multiple modes exist
            if minmode:
                return mode_values.min()
            elif maxmode:
                return mode_values.max()
            elif nummode is not None:
                sorted_modes = mode_values.sort_values()
                if 1 <= nummode <= len(sorted_modes):
                    return sorted_modes.iloc[nummode - 1]
                else:
                    return np.nan
            else:
                return np.nan  # Default behavior when multiple modes exist
    
    if by is None:
        overall_mode = _mode(series)
        return pd.Series([overall_mode] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform(_mode)


def kurt(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate kurtosis, optionally by group.
    
    Equivalent to Stata's: egen newvar = kurt(var) [, by(group)]
    
    Parameters:
    -----------
    series : pd.Series
        Input series
    by : pd.Series, optional
        Grouping variable
        
    Returns:
    --------
    pd.Series
        Kurtosis values (by group if specified)
    """
    _validate_series(series)
    
    if by is None:
        overall_kurt = series.kurtosis()
        return pd.Series([overall_kurt] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform('kurtosis')


def skew(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate skewness, optionally by group.
    
    Equivalent to Stata's: egen newvar = skew(var) [, by(group)]
    
    Parameters:
    -----------
    series : pd.Series
        Input series
    by : pd.Series, optional
        Grouping variable
        
    Returns:
    --------
    pd.Series
        Skewness values (by group if specified)
    """
    _validate_series(series)
    
    if by is None:
        overall_skew = series.skew()
        return pd.Series([overall_skew] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform('skew')


def mad(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate median absolute deviation from the median, optionally by group.
    
    Equivalent to Stata's: egen newvar = mad(var) [, by(group)]
    
    Parameters:
    -----------
    series : pd.Series
        Input series
    by : pd.Series, optional
        Grouping variable
        
    Returns:
    --------
    pd.Series
        MAD values (by group if specified)
    """
    _validate_series(series)
    
    def _mad(x):
        return (x - x.median()).abs().median()
    
    if by is None:
        overall_mad = _mad(series)
        return pd.Series([overall_mad] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform(_mad)


def mdev(series: pd.Series, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate mean absolute deviation from the mean, optionally by group.
    
    Equivalent to Stata's: egen newvar = mdev(var) [, by(group)]
    
    Parameters:
    -----------
    series : pd.Series
        Input series
    by : pd.Series, optional
        Grouping variable
        
    Returns:
    --------
    pd.Series
        Mean absolute deviation values (by group if specified)
    """
    _validate_series(series)
    
    def _mdev(x):
        return (x - x.mean()).abs().mean()
    
    if by is None:
        overall_mdev = _mdev(series)
        return pd.Series([overall_mdev] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform(_mdev)


def pctile(series: pd.Series, p: float = 50, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate percentile, optionally by group.
    
    Equivalent to Stata's: egen newvar = pctile(var), p(#) [by(group)]
    
    Parameters:
    -----------
    series : pd.Series
        Input series
    p : float, default 50
        Percentile to calculate (0-100)
    by : pd.Series, optional
        Grouping variable
        
    Returns:
    --------
    pd.Series
        Percentile values (by group if specified)
    """
    _validate_series(series)
    
    if not 0 <= p <= 100:
        raise ValueError("Percentile p must be between 0 and 100")
    
    if by is None:
        overall_pctile = series.quantile(p/100)
        return pd.Series([overall_pctile] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform(lambda x: x.quantile(p/100))


def std(series: pd.Series, mean_val: float = 0, sd_val: float = 1, 
        by: Optional[pd.Series] = None) -> pd.Series:
    """
    Calculate standardized values, optionally by group.
    
    Equivalent to Stata's: egen newvar = std(var), mean(#) sd(#) [by(group)]
    
    Parameters:
    -----------
    series : pd.Series
        Input series
    mean_val : float, default 0
        Target mean for standardized values
    sd_val : float, default 1
        Target standard deviation for standardized values
    by : pd.Series, optional
        Grouping variable
        
    Returns:
    --------
    pd.Series
        Standardized values (by group if specified)
    """
    _validate_series(series)
    
    def _standardize(x):
        return ((x - x.mean()) / x.std()) * sd_val + mean_val
    
    if by is None:
        return _standardize(series)
    else:
        _validate_series(by)
        return series.groupby(by).transform(_standardize)


def total(series: pd.Series, by: Optional[pd.Series] = None, missing: bool = False) -> pd.Series:
    """
    Calculate total (sum), optionally by group.
    
    Equivalent to Stata's: egen newvar = total(var) [, by(group) missing]
    
    Parameters:
    -----------
    series : pd.Series
        Input series
    by : pd.Series, optional
        Grouping variable
    missing : bool, default False
        If True and all values are missing, return missing instead of 0
        
    Returns:
    --------
    pd.Series
        Total values (by group if specified)
    """
    _validate_series(series)
    
    def _total(x):
        if missing and x.isna().all():
            return np.nan
        return x.sum()
    
    if by is None:
        overall_total = _total(series)
        return pd.Series([overall_total] * len(series), index=series.index)
    else:
        _validate_series(by)
        return series.groupby(by).transform(_total)


# ============================================================================
# Utility Functions
# ============================================================================

def anycount(df: pd.DataFrame, columns: List[str], values: List[Union[int, float]]) -> pd.Series:
    """
    Count variables in varlist equal to any value in values list.
    
    Equivalent to Stata's: egen newvar = anycount(var1-var3), values(1 2 3)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to examine
    values : List[Union[int, float]]
        List of values to match
        
    Returns:
    --------
    pd.Series
        Count of variables matching any value in the list
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    
    def count_matches(row):
        count = 0
        for col in columns:
            if row[col] in values:
                count += 1
        return count
    
    return df[columns].apply(count_matches, axis=1)


def anymatch(df: pd.DataFrame, columns: List[str], values: List[Union[int, float]]) -> pd.Series:
    """
    Check if any variable in varlist equals any value in values list.
    
    Equivalent to Stata's: egen newvar = anymatch(var1-var3), values(1 2 3)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to examine
    values : List[Union[int, float]]
        List of values to match
        
    Returns:
    --------
    pd.Series
        1 if any variable matches, 0 otherwise
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    
    def has_match(row):
        for col in columns:
            if row[col] in values:
                return 1
        return 0
    
    return df[columns].apply(has_match, axis=1)


def anyvalue(series: pd.Series, values: List[Union[int, float]]) -> pd.Series:
    """
    Return value if it matches any value in values list, missing otherwise.
    
    Equivalent to Stata's: egen newvar = anyvalue(var), values(1 2 3)
    
    Parameters:
    -----------
    series : pd.Series
        Input series
    values : List[Union[int, float]]
        List of values to match
        
    Returns:
    --------
    pd.Series
        Original value if it matches, missing otherwise
    """
    _validate_series(series)
    
    return series.where(series.isin(values))


def concat(df: pd.DataFrame, columns: List[str], 
          format_str: Optional[str] = None, decode: bool = False,
          maxlength: Optional[int] = None, punct: str = "") -> pd.Series:
    """
    Concatenate variables to produce a string variable.
    
    Equivalent to Stata's: egen newvar = concat(var1-var3), format() decode maxlength() punct()
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to concatenate
    format_str : str, optional
        Format for numeric variables
    decode : bool, default False
        Decode value labels (not implemented)
    maxlength : int, optional
        Maximum length for each component
    punct : str, default ""
        Punctuation to insert between variables
        
    Returns:
    --------
    pd.Series
        Concatenated string values
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    
    def concatenate_row(row):
        parts = []
        for col in columns:
            val = row[col]
            if pd.isna(val):
                val_str = ""
            elif df[col].dtype in ['int64', 'float64']:
                if format_str:
                    # Simple format handling
                    val_str = format_str % val
                else:
                    val_str = str(val)
            else:
                val_str = str(val)
            
            if maxlength and len(val_str) > maxlength:
                val_str = val_str[:maxlength]
            
            parts.append(val_str)
        
        return punct.join(parts)
    
    return df[columns].apply(concatenate_row, axis=1)


def cut(series: pd.Series, at: Optional[List[float]] = None, 
        group: Optional[int] = None, icodes: bool = False, 
        label: bool = False) -> pd.Series:
    """
    Create categorical variable from continuous variable.
    
    Equivalent to Stata's: egen newvar = cut(var), at() group() icodes label
    
    Parameters:
    -----------
    series : pd.Series
        Input series to cut
    at : List[float], optional
        Breakpoints for groups
    group : int, optional
        Number of equal-frequency groups
    icodes : bool, default False
        Use integer codes instead of interval labels
    label : bool, default False
        Add value labels (automatically invokes icodes)
        
    Returns:
    --------
    pd.Series
        Categorical variable
    """
    _validate_series(series)
    
    if at is None and group is None:
        raise ValueError("Either 'at' or 'group' must be specified")
    if at is not None and group is not None:
        raise ValueError("Cannot specify both 'at' and 'group'")
    
    if at is not None:
        # Use specified breakpoints
        result = pd.cut(series, bins=at, right=False, include_lowest=True)
        if icodes or label:
            result = result.cat.codes + 1  # Stata uses 1-based indexing
            result = result.replace(-1, np.nan)  # Missing for out-of-range values
    else:
        # Use equal-frequency groups
        result = pd.qcut(series, q=group, duplicates='drop')
        if icodes or label:
            result = result.cat.codes + 1
    
    return result


def diff(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Create indicator variable showing if variables are not all equal.
    
    Equivalent to Stata's: egen newvar = diff(var1-var3)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to compare
        
    Returns:
    --------
    pd.Series
        1 if variables differ, 0 if all equal
    """
    _validate_dataframe(df)
    _validate_columns(df, columns)
    
    def check_diff(row):
        values = [row[col] for col in columns if pd.notna(row[col])]
        if len(values) <= 1:
            return 0
        return 1 if len(set(values)) > 1 else 0
    
    return df[columns].apply(check_diff, axis=1)


def ends(series: pd.Series, punct: str = " ", trim: bool = False,
         head: bool = False, last: bool = False, tail: bool = False) -> pd.Series:
    """
    Extract parts of string variable.
    
    Equivalent to Stata's: egen newvar = ends(strvar), punct() trim head|last|tail
    
    Parameters:
    -----------
    series : pd.Series
        Input string series
    punct : str, default " "
        Punctuation character to split on
    trim : bool, default False
        Trim leading/trailing spaces
    head : bool, default False
        Extract first part (before first punct)
    last : bool, default False
        Extract last part (after last punct)
    tail : bool, default False
        Extract remainder (after first punct)
        
    Returns:
    --------
    pd.Series
        Extracted string parts
    """
    _validate_series(series)
    
    # Use builtins.sum to avoid conflict with pyegen.sum()
    if __builtins__['sum']([head, last, tail]) != 1:
        raise ValueError("Exactly one of head, last, or tail must be True")
    
    def extract_part(s):
        if pd.isna(s):
            return s
        
        s = str(s)
        if trim:
            s = s.strip()
        
        if punct not in s:
            if head or last:
                return s
            else:  # tail
                return ""
        
        if head:
            return s.split(punct, 1)[0]
        elif last:
            return s.rsplit(punct, 1)[1]
        else:  # tail
            return s.split(punct, 1)[1]
    
    return series.apply(extract_part)


def fill(numlist: List[float], length: int) -> pd.Series:
    """
    Create variable with repeating pattern from numlist.
    
    Equivalent to Stata's: egen newvar = fill(numlist)
    
    Parameters:
    -----------
    numlist : List[float]
        List of numbers to repeat
    length : int
        Length of series to create
        
    Returns:
    --------
    pd.Series
        Series with repeating pattern
    """
    if len(numlist) < 2:
        raise ValueError("numlist must contain at least two numbers")
    
    # Repeat the pattern to fill the required length
    repeated = (numlist * ((length // len(numlist)) + 1))[:length]
    return pd.Series(repeated)


# ============================================================================
# Sequence Functions
# ============================================================================

def seq(length: Optional[int] = None, from_val: int = 1, to_val: Optional[int] = None, 
        block: int = 1, by: Optional[pd.Series] = None) -> pd.Series:
    """
    Generate integer sequences.
    
    Equivalent to Stata's: egen newvar = seq(), from() to() block() [by(group)]
    
    Parameters:
    -----------
    length : int, optional
        Length of sequence to generate
    from_val : int, default 1
        Starting value
    to_val : int, optional
        Ending value (default is length)
    block : int, default 1
        Block size for repetition
    by : pd.Series, optional
        Grouping variable
        
    Returns:
    --------
    pd.Series
        Integer sequence
    """
    if length is None and to_val is None:
        raise ValueError("Either 'length' or 'to_val' must be specified")
    
    if length is None:
        length = to_val - from_val + 1
    
    if to_val is None:
        to_val = from_val + length - 1
    
    if by is None:
        # Simple sequence
        result = []
        current = from_val
        for i in range(length):
            if i > 0 and i % block == 0:
                current += 1
                if current > to_val:
                    current = from_val
            result.append(current)
        return pd.Series(result)
    else:
        # Grouped sequence
        _validate_series(by)
        result = []
        for group_val in by.unique():
            group_mask = by == group_val
            group_length = group_mask.sum()
            group_seq = seq(group_length, from_val, to_val, block, by=None)
            result.extend(group_seq.tolist())
        return pd.Series(result, index=by.index)
