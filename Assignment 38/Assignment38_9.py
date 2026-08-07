# Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.

import pandas as pd
import matplotlib.pyplot as plt

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

# Calculate average assignments completed for each result

AssignmentAvg = df.groupby("FinalResult")["AssignmentsCompleted"].mean()

plt.figure(figsize=(6,4))

plt.bar(["Fail", "Pass"], AssignmentAvg, color=["red", "green"])

plt.title("Average Assignments Completed vs Final Result")

plt.xlabel("Final Result")

plt.ylabel("Average Assignments Completed")

plt.show()

print("""
Observation
-Pass students have completed more assignments on average than Fail students.
-Students who complete more assignments are more likely to pass.
-This indicates a positive relationship between assignment completion and academic performance.
-Completing assignments regularly improves the chances of passing.
""")