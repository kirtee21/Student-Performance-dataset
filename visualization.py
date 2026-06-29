import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("student-mat.csv", sep=";")

# Histogram
plt.figure()
plt.hist(df["G3"], bins=10)
plt.title("Histogram of Grades")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(df["studytime"], df["G3"])
plt.title("Study Time vs Grades")
plt.xlabel("Study Time")
plt.ylabel("Grades")
plt.show()

# Bar Chart
gender_avg = df.groupby("sex")["G3"].mean()

plt.figure()
plt.bar(gender_avg.index, gender_avg.values)
plt.title("Male vs Female Average Score")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.show()