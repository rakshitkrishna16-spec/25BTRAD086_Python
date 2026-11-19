log_data = """[INFO] System initialized.
[WARNING] Disk space low.
[ERROR] Database connection failed.
[INFO] User logged in.
[ERROR] Timeout error."""

counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

for line in log_data.strip().split("\n"):
    for key in counts:
        if key in line:
            counts[key] += 1

print("Log Summary:")
for level, count in counts.items():
    print(f"{level}: {count}")