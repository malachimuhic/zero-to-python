# students = ["Hermoine", "Harry", "Ron"]

# print(students[0])

# for names in students:
#     print(names) 

# for i in range(len(students)):
#     print(i + 1, students[i])



# ==============================
# Dictionaries
# ==============================

# students={}

# for student in students:
#     print(student, students[student], sep=", ")

students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ") 