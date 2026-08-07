# Plot a histogram of StudyHours.
# Explain what the distribution tells you

import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*100

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

plt.figure(figsize=(6,4))

plt.hist(df["StudyHours"], bins=5, edgecolor="black")

plt.title("Histogram of StudyHours")

plt.xlabel("Study Hours")

plt.ylabel("Number of Students")

plt.show()

print("""Observation
    - The histogram shows that StudyHours are distributed between 1 and 8 hours.
    - Most students study between 5 and 8 hours, as these bars have relatively higher frequencies.
    - Fewer students study for 1–3 hours compared to the higher study-hour ranges.
    - The distribution indicates that a majority of students spend a moderate to high number of hours studying.
    - There are no extreme outliers, and the study hours appear to be fairly evenly distributed.""")



