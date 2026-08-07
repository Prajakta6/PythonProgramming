# Draw a boxplot for Attendance.
# Identify if any outliers are present.

import pandas as pd
import matplotlib.pyplot as plt

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)
plt.boxplot(df["Attendance"])
plt.title("Box Plot for Attendance")
plt.ylabel("Values")
plt.show()

print("""
Observation
-The Attendance values range approximately from 60 to 96.
-The median attendance is around 80 (orange line inside the box).
-The middle 50% of attendance values lie approximately between 70 (Q1) and 89 (Q3).
-No data points are visible outside the whiskers.
-Therefore, there are no outliers present in the Attendance column.""")

#OUTPUT
#         Maximum value
#              |
#              |
#           ───┐   ← Upper whisker
#              │
#         ┌─────────┐
#  Q3 --->│         │
#  Median>│─────────│
#  Q1 --->│         │
#         └─────────┘
#              │
#           ───┘   ← Lower whisker
#              |
#              |
#         Minimum value