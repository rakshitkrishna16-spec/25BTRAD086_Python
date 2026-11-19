# Write records
with open("students.txt", "w") as f:
    f.write("101, Rahul, Computer Science\n")
    f.write("102, Ananya, Data Science\n")

# Read records
print("Student Records from File:")
with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())