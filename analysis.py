import pandas as pd

# Load dataset
df = pd.read_csv("student-mat.csv", sep=";")

# 1. Average Final Grade (G3)
average_g3 = df["G3"].mean()
print("Average Final Grade (G3):", average_g3)

# 2. Students Scored Above 15
above_15 = df[df["G3"] > 15].shape[0]
print("Students Scored Above 15:", above_15)

# 3. Correlation Between Study Time and Performance
correlation = df["studytime"].corr(df["G3"])
print("Correlation Between Study Time and G3:", correlation)

# 4. Average Performance by Gender
gender_performance = df.groupby("sex")["G3"].mean()
print("Average Performance by Gender:")
print(gender_performance)