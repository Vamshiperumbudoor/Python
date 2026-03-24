import pandas as pd

# Load a dataset (usually a CSV)
df = pd.read_csv('data.csv')

# Look at the first 5 rows
print(df.head())

# Get the "meta" view: data types, null counts, and memory usage
df.info()




# Calculate the average salary for each department
df.groupby('department')['salary'].mean()

# Get multiple stats at once
df.groupby('city').agg({'temperature': 'mean', 'humidity': 'max'})




# Statistical summary of all numerical columns
df.describe()

# Count how many times each value appears (great for categories)
df['category'].value_counts()

# Sort your data
df.sort_values(by='price', ascending=False)


