import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
data = pd.read_csv("dataset.csv")

# Clean data
data = data.dropna()

# Basic analysis
average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

print("\n===== Student Performance Report =====")
print(f"Total Students: {len(data)}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")

# Top students
top_students = data.sort_values(
    by="Marks",
    ascending=False
).head(5)

print("\nTop 5 Students:")
print(top_students)

# Create chart
plt.figure(figsize=(8, 5))
plt.hist(data["Marks"])

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.savefig("marks_distribution.png")

print("\nChart saved: marks_distribution.png")
