def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

print(f"Student: {name} | Marks: {marks} | Grade: {calculate_grade(marks)}")