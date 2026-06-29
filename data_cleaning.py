import pandas as pd

# Load dataset
df = pd.read_csv("student-mat.csv", sep=";")

# 1. Check Missing Values
print("Missing Values:")
print(df.isnull().sum())

# 2. Remove Duplicates
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print("\nDuplicate Rows Removed:", before - after)

# 3. Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# 4. Data Types
print("\nData Types:")
print(df.dtypes)