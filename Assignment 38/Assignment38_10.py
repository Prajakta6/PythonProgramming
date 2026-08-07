# Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

# Calculate average SleepHours for Pass and Fail students
SleepAvg = df.groupby("FinalResult")["SleepHours"].mean()

plt.figure(figsize=(6,4))

plt.bar(["Fail", "Pass"], SleepAvg, color=["red", "green"])

plt.title("Average Sleep Hours vs Final Result")
plt.xlabel("Final Result")
plt.ylabel("Average Sleep Hours")
plt.legend()
plt.show()

print("""
Observation
- Pass and Fail students may have different average sleep hours.
- Students who get adequate sleep may perform better because they are more focused and attentive.
- However, sleeping more does not guarantee success.
- Academic performance also depends on factors such as StudyHours, Attendance, PreviousScore, and AssignmentsCompleted.
- Therefore, sleep is an important factor, but it is not the only factor affecting the FinalResult.""")