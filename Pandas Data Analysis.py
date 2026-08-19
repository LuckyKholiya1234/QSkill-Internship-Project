import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV file
data = pd.read_csv("students.csv")


# Display the data
print("Student Data:")
print(data)


# Display first 5 rows
print("\nFirst 5 rows:")
print(data.head())


# Display basic information
print("\nInformation about the data:")
print(data.info())


# Calculate average marks
math_average = data["Math"].mean()
science_average = data["Science"].mean()
english_average = data["English"].mean()

print("\nAverage Marks:")
print("Math:", round(math_average, 2))
print("Science:", round(science_average, 2))
print("English:", round(english_average, 2))


# Find highest marks in each subject
print("\nHighest Marks:")
print("Math:", data["Math"].max())
print("Science:", data["Science"].max())
print("English:", data["English"].max())


# Find lowest marks in each subject
print("\nLowest Marks:")
print("Math:", data["Math"].min())
print("Science:", data["Science"].min())
print("English:", data["English"].min())


# Create a total marks column
data["Total"] = data["Math"] + data["Science"] + data["English"]


# Create an average marks column
data["Average"] = data["Total"] / 3


print("\nData after adding Total and Average:")
print(data)


# Find the student with highest total marks
highest_student = data.loc[data["Total"].idxmax()]

print("\nStudent with highest marks:")
print(highest_student["Name"])
print("Total Marks:", highest_student["Total"])


# -------------------------------
# BAR CHART
# -------------------------------

subjects = ["Math", "Science", "English"]
averages = [
    math_average,
    science_average,
    english_average
]

plt.figure(figsize=(7, 5))

plt.bar(subjects, averages)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()


# -------------------------------
# SCATTER PLOT
# -------------------------------

plt.figure(figsize=(7, 5))

plt.scatter(data["Math"], data["Science"])

plt.title("Math Marks vs Science Marks")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")

plt.show()


# -------------------------------
# HEATMAP
# -------------------------------

# Select only numerical columns
numeric_data = data[["Age", "Math", "Science", "English", "Total", "Average"]]

# Calculate correlation
correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))

plt.imshow(correlation, cmap="coolwarm")

plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Heatmap")

plt.show()


# -------------------------------
# BASIC OBSERVATIONS
# -------------------------------

print("\nObservations:")

print(
    "1. The average marks in Math are",
    round(math_average, 2)
)

print(
    "2. The average marks in Science are",
    round(science_average, 2)
)

print(
    "3. The average marks in English are",
    round(english_average, 2)
)

print(
    "4. The student with the highest total marks is",
    highest_student["Name"]
)

print(
    "5. The highest total marks are",
    highest_student["Total"]
)