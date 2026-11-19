# Dictionary storing student names and list of daily statuses ('P' or 'A')
attendance = {
    "Rakshit": ["P", "P", "A", "P", "P"],
    "Ruchitha": ["P", "P", "P", "P", "P"],
    "Fathima": ["P", "A", "A", "P", "A"]
}

def add_student(name):
    if name not in attendance:
        attendance[name] = []
        print(f"Added student: {name}")
    else:
        print(f"{name} already exists.")

def mark_attendance(name, status):
    if name in attendance:
        attendance[name].append(status.upper())
        print(f"Marked {status.upper()} for {name}")
    else:
        print("Student not found.")

def display_report(threshold=75.0):
    print("\n--- ATTENDANCE REPORT ---")
    low_attendance = []
    
    for name, records in attendance.items():
        total_classes = len(records)
        if total_classes == 0:
            percentage = 0.0
        else:
            present_count = records.count("P")
            percentage = (present_count / total_classes) * 100
        
        print(f"Student: {name:<10} | Records: {records} | Attendance: {percentage:.2f}%")
        
        if percentage < threshold:
            low_attendance.append((name, percentage))
            
    print(f"\nStudents below {threshold}% threshold:")
    for name, pct in low_attendance:
        print(f"- {name} ({pct:.2f}%)")

# Testing the functionalities
add_student("Rio")
mark_attendance("Rio", "P")
mark_attendance("Rio", "A")
mark_attendance("Fathima", "P")
display_report(threshold=75.0)