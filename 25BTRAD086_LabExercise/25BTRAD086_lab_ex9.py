students = {"Rahul": 92, "Ananya": 78, "Kiran": 45}

for name, marks in students.items():
    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 50:
        grade = "B"
    else:
        grade = "Fail"
    print(f"Student: {name} | Marks: {marks} | Grade: {grade}")