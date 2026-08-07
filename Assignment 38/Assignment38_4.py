# Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.

import pandas as pd

Border = "-"*100
print(Border)

DataPath =  "student_performance_ml.csv"
df = pd.read_csv(DataPath)

print("Data loaded successfully")
print(Border)
FinalResult_distribution = df["FinalResult"].value_counts()
print(f"Distribution of FinalResult is : {FinalResult_distribution}")

Pass_Count = (df["FinalResult"] == 1).sum()
Fail_Count = (df["FinalResult"] == 0).sum()
Total_Students = len(df)

Pass_Percentage = (Pass_Count / Total_Students) * 100
Fail_Percentage = (Fail_Count / Total_Students) * 100
print(Border)
print(f"Pass Students      : {Pass_Count}")
print(f"Fail Students      : {Fail_Count}")
print(f"Pass Percentage    : {Pass_Percentage:.2f}%")
print(f"Fail Percentage    : {Fail_Percentage:.2f}%")

if abs(Pass_Percentage - Fail_Percentage) <= 10:
    print("\nThe dataset is balanced because the percentages of Pass and Fail are nearly equal.")
else:
    print("\nThe dataset is imbalanced because one class has significantly more samples than the other.")
    
print(Border)

#OUTPUT
# ----------------------------------------------------------------------------------------------------
# Data loaded successfully
# ----------------------------------------------------------------------------------------------------
# Distribution of FinalResult is : FinalResult
# 1    18
# 0    12
# Name: count, dtype: int64
# ----------------------------------------------------------------------------------------------------
# Pass Students      : 18
# Fail Students      : 12
# Pass Percentage    : 60.00%
# Fail Percentage    : 40.00%

# The dataset is imbalanced because one class has significantly more samples than the other.
# ----------------------------------------------------------------------------------------------------
