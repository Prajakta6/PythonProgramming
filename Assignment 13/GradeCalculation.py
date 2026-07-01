# Write a program which accepts marks and displays grade.
# Condition Example:
# ≥ 75 → Distinction
# ≥ 60 → First Class
# ≥ 50 → Second Class
# < 50 → Fail

def calculate_grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"

def main():
    marks = int(input("Enetr your marks: "))
    result = calculate_grade(marks)
    print("Your grade is : ", result)

if __name__ == "__main__":
    main()

#OUTPUT
# Enetr your marks: 90
# Your grade is :  Distinction
# Enetr your marks: 70
# Your grade is :  First Class
# Enetr your marks: 55
# Your grade is :  Second Class
# Enetr your marks: 45
# Your grade is :  Fail