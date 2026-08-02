student = {
    "name": "ali",
    "age": 20,
    "average": 15.5
}

print(f"the name of student is {student['name']}")

student['age'] = 30
student['city'] = "oran"

for value in student.items():
    print(value)