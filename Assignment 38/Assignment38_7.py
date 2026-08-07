# Create a scatter plot of:
# StudyHours vs PreviousScore
# Use different colors for Pass and Fail students.

import pandas as pd
import matplotlib.pyplot as plt

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

# Separate Pass & Fail students
Pass = df[df["FinalResult"] == 1]
Fail = df[df["FinalResult"] == 0]
plt.figure(figsize=(6,4))

# Pass students (Green)
plt.scatter(Pass["StudyHours"], Pass["PreviousScore"], color="green", label="Pass")

# Fail students (Red)
plt.scatter(Fail["StudyHours"], Fail["PreviousScore"], color="red", label="Fail")

plt.title("StudyHours vs PreviousScore")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.legend(loc="best")
plt.show()