# Import pandas
import pandas as pd

# Load the dataset
df = pd.read_csv("student-mat.csv", sep=";")

# Display the first 5 rows
print(df.head())