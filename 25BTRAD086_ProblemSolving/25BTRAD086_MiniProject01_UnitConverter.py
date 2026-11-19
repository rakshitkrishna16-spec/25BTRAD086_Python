print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
print("3. Kilograms to Pounds")

choice = int(input("Choose conversion (1-3): "))
val = float(input("Enter value: "))

if choice == 1:
    print(f"{val} km = {val * 0.621371:.2f} miles")
elif choice == 2:
    print(f"{val} C = {(val * 9 / 5) + 32:.2f} F")
elif choice == 3:
    print(f"{val} kg = {val * 2.20462:.2f} lbs")
else:
    print("Invalid choice")