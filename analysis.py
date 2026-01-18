import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# PROJECT SETUP
# -------------------------------
DATA_PATH = r"C:\Users\Ahana Chatterjee\Desktop\PROJECTS\Student Performance Analysis\data"
FILE_PATH = os.path.join(DATA_PATH, "student_data.csv")

os.makedirs(DATA_PATH, exist_ok=True)

# -------------------------------
# LOAD DATA
# -------------------------------
data = pd.read_csv(FILE_PATH)

print("\n=== STUDENT DATA LOADED SUCCESSFULLY ===\n")
print(data.head())

# -------------------------------
# BASIC EXPLORATION
# -------------------------------
print("\n=== DATA INFO ===")
print(data.info())

print("\n=== STATISTICAL SUMMARY ===")
print(data.describe())

# -------------------------------
# AGGREGATIONS
# -------------------------------
avg_marks_subject = data.groupby("subject")["marks"].mean()
avg_marks_gender = data.groupby("gender")["marks"].mean()

# -------------------------------
# VISUAL 1: ATTENDANCE VS MARKS
# -------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(data["attendance"], data["marks"])
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.title("Attendance vs Marks")
plt.grid(True)
plt.savefig(os.path.join(DATA_PATH, "attendance_vs_marks.png"))
plt.show()

# -------------------------------
# VISUAL 2: STUDY HOURS VS MARKS
# -------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(data["study_hours"], data["marks"])
plt.xlabel("Study Hours per Day")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.grid(True)
plt.savefig(os.path.join(DATA_PATH, "study_hours_vs_marks.png"))
plt.show()

# -------------------------------
# VISUAL 3: SUBJECT-WISE AVERAGE MARKS
# -------------------------------
plt.figure(figsize=(8, 5))
avg_marks_subject.plot(kind="bar")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.title("Average Marks by Subject")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig(os.path.join(DATA_PATH, "avg_marks_by_subject.png"))
plt.show()

# -------------------------------
# VISUAL 4: GENDER-WISE AVERAGE MARKS
# -------------------------------
plt.figure(figsize=(6, 5))
avg_marks_gender.plot(kind="bar")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.title("Average Marks by Gender")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig(os.path.join(DATA_PATH, "avg_marks_by_gender.png"))
plt.show()

# -------------------------------
# TOP PERFORMERS
# -------------------------------
top_students = data.sort_values(by="marks", ascending=False).head(3)
print("\n=== TOP 3 STUDENTS ===")
print(top_students[["name", "subject", "marks"]])

# -------------------------------
# PERFORMANCE CATEGORY
# -------------------------------
data["performance"] = data["marks"].apply(
    lambda x: "Excellent" if x >= 85 else "Good" if x >= 70 else "Needs Improvement"
)

# -------------------------------
# CORRELATION ANALYSIS
# -------------------------------
correlation = data[["marks", "attendance", "study_hours"]].corr()
print("\n=== CORRELATION MATRIX ===")
print(correlation)

# -------------------------------
# SAVE FINAL REPORT
# -------------------------------
FINAL_REPORT = os.path.join(DATA_PATH, "student_final_report.csv")
data.to_csv(FINAL_REPORT, index=False)

print("\n=== PROJECT COMPLETED SUCCESSFULLY ===")
print("Final report saved as: student_final_report.csv")
print("All graphs saved inside data folder.")
