csv_data = """EmpID,Name,Basic
1,Alice,50000
2,Bob,60000"""

lines = csv_data.strip().split("\n")[1:]

print("Payroll Summary:")
for line in lines:
    emp_id, name, basic = line.split(",")
    basic = float(basic)
    tax = basic * 0.10
    net_salary = basic - tax
    print(f"ID: {emp_id} | Name: {name} | Net Salary: {net_salary:.2f}")