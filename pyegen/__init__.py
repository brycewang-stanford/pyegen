"""
PyEgen: Python implementation of Stata's egen command

This package provides Stata-style data manipulation functions for pandas DataFrames,
making it easier for researchers to transition from Stata to Python.
"""

__version__ = "0.2.2"

from .core import (
    # Basic functions
    rank,
    rowmean,
    rowtotal,
    rowmax,
    rowmin,
    rowcount,
    rowsd,
    
    # New row-wise functions
    rowfirst,
    rowlast,
    rowmedian,
    rowmiss,
    rownonmiss,
    rowpctile,
    
    # Grouping functions
    tag,
    count,
    mean,
    sum,
    max,
    min,
    sd,
    
    # Statistical functions
    median,
    mode,
    kurt,
    skew,
    mad,
    mdev,
    pctile,
    std,
    total,
    
    # Utility functions
    anycount,
    anymatch,
    anyvalue,
    concat,
    cut,
    diff,
    ends,
    fill,
    
    # Advanced functions
    seq,
    group,
    pc,
    iqr,
)

__all__ = [
    # Basic functions
    "rank",
    "rowmean", 
    "rowtotal",
    "rowmax",
    "rowmin",
    "rowcount",
    "rowsd",
    
    # New row-wise functions
    "rowfirst",
    "rowlast", 
    "rowmedian",
    "rowmiss",
    "rownonmiss",
    "rowpctile",
    
    # Grouping functions
    "tag",
    "count",
    "mean",
    "sum",
    "max",
    "min", 
    "sd",
    
    # Statistical functions
    "median",
    "mode",
    "kurt",
    "skew",
    "mad",
    "mdev",
    "pctile",
    "std",
    "total",
    
    # Utility functions
    "anycount",
    "anymatch",
    "anyvalue",
    "concat",
    "cut",
    "diff",
    "ends",
    "fill",
    
    # Advanced functions
    "seq",
    "group",
    "pc",
    "iqr",
    
    "__version__",
]
