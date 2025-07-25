"""
PyEgen Examples

This file demonstrates the usage of PyEgen functions with practical examples.
"""

import pandas as pd
import numpy as np
import pyegen as egen

# Create sample data
print("=== PyEgen Examples ===\n")

# Sample dataset
df = pd.DataFrame({
    'country': ['USA', 'USA', 'CHN', 'CHN', 'DEU', 'DEU', 'JPN', 'JPN'],
    'year': [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021],
    'gdp': [21.43, 22.32, 14.72, 17.73, 3.84, 4.26, 4.94, 4.24],
    'population': [331, 332, 1439, 1412, 83, 83, 125, 124],
    'exports': [1.65, 1.76, 2.64, 3.36, 1.56, 1.73, 0.71, 0.76]
})

print("Original Dataset:")
print(df)
print("\n")

# Example 1: Basic row operations
print("1. Row Operations:")
df['gdp_pop_mean'] = egen.rowmean(df, ['gdp', 'population'])
df['gdp_exports_total'] = egen.rowtotal(df, ['gdp', 'exports'])
df['max_economic'] = egen.rowmax(df, ['gdp', 'exports'])

print("After adding row statistics:")
print(df[['country', 'year', 'gdp', 'exports', 'gdp_pop_mean', 'gdp_exports_total', 'max_economic']])
print("\n")

# Example 2: Ranking
print("2. Ranking:")
df['gdp_rank'] = egen.rank(df['gdp'])
df['gdp_rank_desc'] = egen.rank(df['gdp'], ascending=False)

print("With rankings:")
print(df[['country', 'year', 'gdp', 'gdp_rank', 'gdp_rank_desc']])
print("\n")

# Example 3: Group operations
print("3. Group Operations:")
df['mean_gdp_by_country'] = egen.mean(df['gdp'], by=df['country'])
df['max_gdp_by_country'] = egen.max(df['gdp'], by=df['country'])
df['country_tag'] = egen.tag(df, ['country'])
df['obs_per_country'] = egen.count(df['gdp'], by=df['country'])

print("With group statistics:")
print(df[['country', 'year', 'gdp', 'mean_gdp_by_country', 'max_gdp_by_country', 'country_tag', 'obs_per_country']])
print("\n")

# Example 4: Group identifiers
print("4. Group Identifiers:")
df['country_id'] = egen.group(df, ['country'])
df['country_year_id'] = egen.group(df, ['country', 'year'])

print("With group IDs:")
print(df[['country', 'year', 'country_id', 'country_year_id']])
print("\n")

# Example 5: Working with missing values
print("5. Missing Values Example:")
df_missing = pd.DataFrame({
    'var1': [1, 2, np.nan, 4, 5],
    'var2': [10, np.nan, 30, 40, np.nan],
    'var3': [100, 200, 300, np.nan, 500],
    'group': ['A', 'A', 'B', 'B', 'C']
})

df_missing['row_mean'] = egen.rowmean(df_missing, ['var1', 'var2', 'var3'])
df_missing['row_count'] = egen.rowcount(df_missing, ['var1', 'var2', 'var3'])
df_missing['group_mean'] = egen.mean(df_missing['var1'], by=df_missing['group'])

print("Dataset with missing values:")
print(df_missing)
print("\n")

# Example 6: Percentiles
print("6. Percentiles:")
df['gdp_percentile'] = egen.pc(df['gdp'])
df['gdp_percentile_by_year'] = egen.pc(df['gdp'], by=df['year'])

print("With percentiles:")
print(df[['country', 'year', 'gdp', 'gdp_percentile', 'gdp_percentile_by_year']])
print("\n")

print("=== All examples completed successfully! ===")

if __name__ == "__main__":
    print("\nRun this file to see PyEgen in action!")
    print("python examples.py")
