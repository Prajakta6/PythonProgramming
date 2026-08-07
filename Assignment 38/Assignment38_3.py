# Using pandas functions, calculate and display:
# • Average StudyHours
# • Average Attendance
# • Maximum PreviousScore
# • Minimum SleepHours

import pandas as pd
print("\n")
Border = "-"*100

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully")
print(Border)
avg_study_hours = df["StudyHours"].mean()
print(f"\nAverage StudyHours is : {avg_study_hours}")
print(Border)
avg_attendance = df["Attendance"].mean()
print(f"\nAverage Attendance is : {avg_attendance}")
print(Border)
max_previous_score = df["PreviousScore"].max()
print(f"\nMaximum PreviousScore is {max_previous_score}")
print(Border)
min_sleep_hours = df["SleepHours"].min()
print(f"\nMinimum SleepHours is {min_sleep_hours}")
print(Border)

#OUTPUT
# Dataset loaded successfully
# ----------------------------------------------------------------------------------------------------

# Average StudyHours is : 4.843333333333333
# ----------------------------------------------------------------------------------------------------

# Average Attendance is : 79.06666666666666
# ----------------------------------------------------------------------------------------------------

# Maximum PreviousScore is 80
# ----------------------------------------------------------------------------------------------------

# Minimum SleepHours is 5
# ----------------------------------------------------------------------------------------------------
