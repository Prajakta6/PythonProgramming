# Write a program to:
# • Display total number of students in the dataset
# • Count how many students Passed (FinalResult = 1)
# • Count how many students Failed (FinalResult = 0)

import pandas as pd
print("\n")
Border = "-"*100

print(Border)
print("Load the dataset - student_performance_ml. csv")
print(Border)

DataPath = "student_performance_ml.csv" #Relative path in current directory

df = pd.read_csv(DataPath) # df is data frame

print("\nDataset loaded successfully.")
print(Border)
print("\nTotal number of students in the dataset are: \n")
print(len(df))
print(Border)
print("\nCount of how many students Passed (FinalResult = 1) : ")
passed_count = (df['FinalResult'] == 1).sum()
print(passed_count)
print(Border)
print("\nCount of how many students Failed (FinalResult = 0) : ")
failed_count = (df['FinalResult'] == 0).sum()
print(failed_count)
print(Border)

# OUTPUT
# ----------------------------------------------------------------------------------------------------
# Load the dataset - student_performance_ml. csv
# ----------------------------------------------------------------------------------------------------

# Dataset loaded successfully.
# ----------------------------------------------------------------------------------------------------

# Total number of students in the dataset are: 

# 30
# ----------------------------------------------------------------------------------------------------

# Count of how many students Passed (FinalResult = 1) : 
# 18
# ----------------------------------------------------------------------------------------------------

# Count of how many students Failed (FinalResult = 0) : 
# 12
# ----------------------------------------------------------------------------------------------------