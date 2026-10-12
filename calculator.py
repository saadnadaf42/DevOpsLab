name = input("Enter Student Name: ")

try:
    marks = float(input("Enter Marks: "))
except ValueError:
    print("Invalid input: marks must be a number.")
    raise SystemExit

if not 0 <= marks <= 100:
    print("Invalid input: marks must be between 0 and 100.")
    raise SystemExit

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)