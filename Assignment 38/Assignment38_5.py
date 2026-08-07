# 5. Based on the dataset values, analyze whether:
# • Higher StudyHours increase the chance of passing.
# • Higher Attendance improves FinalResult.
# Write your observations in 4-5 lines.

import pandas as pd

Border = "-"*100
DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

Analysis = df.groupby("FinalResult")[["StudyHours", "Attendance"]].mean()
print(Border)
print("\nAverage StudyHours and Attendance:\n")
print(Analysis)
print(Border)
print("\nObservations:")

if Analysis.loc[1, "StudyHours"] > Analysis.loc[0, "StudyHours"]:
    print("- Students who passed have higher average StudyHours.")
    print("- Higher StudyHours increase the chance of passing.")
else:
    print("- StudyHours do not appear to increase the chance of passing.")

if Analysis.loc[1, "Attendance"] > Analysis.loc[0, "Attendance"]:
    print("- Students who passed have higher average Attendance.")
    print("- Higher Attendance improves the FinalResult.")
else:
    print("- Attendance does not appear to have a strong effect on the FinalResult.")

print(Border)

#OUTPUT
# ----------------------------------------------------------------------------------------------------

# Average StudyHours and Attendance:

#              StudyHours  Attendance
# FinalResult                        
# 0              2.550000   67.750000
# 1              6.372222   86.611111
# ----------------------------------------------------------------------------------------------------

# Observations:
# - Students who passed have higher average StudyHours.
# - Higher StudyHours increase the chance of passing.
# - Students who passed have higher average Attendance.
# - Higher Attendance improves the FinalResult.
# ----------------------------------------------------------------------------------------------------