import pandas as pd

# Load a dataset (usually a CSV)
df = pd.read_csv('data.csv')

# Look at the first 5 rows
print(df.head())

# Get the "meta" view: data types, null counts, and memory usage
df.info()

