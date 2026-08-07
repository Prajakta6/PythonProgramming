# Write a Python program to load the file student_performance_ml. csv using pandas.
# Display:
# • First 5 records
# • Last 5 records
# • Total number of rows and columns
# • List of column names
# • Data types of each column

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
print("\nFirst 5 enteries from dataset are: \n")
print(df.head())
print(Border)
print("\nLast 5 enteries from dataset are: \n")
print(df.tail())
print(Border)
print("\nTotal number of rows and columns from dataset are: \n")
print(df.shape)
print(Border)
print("\nList of column names from dataset are: \n")
print(df.columns)
print(Border)
print("\nData types of each column from dataset are: \n")
print(df.dtypes)
print(Border)

# OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 38 % python Assignment38_1.py


# ----------------------------------------------------------------------------------------------------
# Load the dataset - student_performance_ml. csv
# ----------------------------------------------------------------------------------------------------

# Dataset loaded successfully.
# ----------------------------------------------------------------------------------------------------

# First 5 enteries from dataset are: 

#    StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours  FinalResult
# 0         2.0          65             45                     3           5            0
# 1         3.0          70             50                     4           6            0
# 2         4.0          75             55                     5           6            0
# 3         5.0          80             60                     6           7            1
# 4         6.0          85             65                     7           7            1
# ----------------------------------------------------------------------------------------------------

# Last 5 enteries from dataset are: 

#     StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours  FinalResult
# 25         5.2          81             61                     6           7            1
# 26         6.2          87             66                     7           7            1
# 27         7.2          91             72                     8           8            1
# 28         8.2          96             78                     9           8            1
# 29         1.8          63             44                     2           5            0
# ----------------------------------------------------------------------------------------------------

# Total number of rows and columns from dataset are: 

# (30, 6)
# ----------------------------------------------------------------------------------------------------

# List of column names from dataset are: 

# Index(['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted',
#        'SleepHours', 'FinalResult'],
#       dtype='object')
# ----------------------------------------------------------------------------------------------------

# Data types of each column from dataset are: 

# StudyHours              float64
# Attendance                int64
# PreviousScore             int64
# AssignmentsCompleted      int64
# SleepHours                int64
# FinalResult               int64
# dtype: object
# ----------------------------------------------------------------------------------------------------
