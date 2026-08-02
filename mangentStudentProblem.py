students = []
number_of_students = int(input("Entrer the number of students:"))
for i in range(number_of_students):
    print(f"\nStudent {i + 1}")
    name = str(input("Entrer the name of student:"))
    age = int(input("Entrer the age of student:"))
    average= float(input("etrer the avrage of student:"))
    student ={
        "name": name,
        "age": age,
        "average": average
    }
    students.append(student)
    print("\n===== STUDENTS =====")

for student in students:
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Average: {student['average']}")
    print("----------------------")