def main():
    #list
    # students = ["Harry", "Hermione", "Ron"]

    #dictionary
    # students = {
    #     "Harry": "Gryffindor",
    #     "Hermione": "Gryffindor",
    #     "Ron": "Gryffindor",
    #     "Draco": "Slytherin"
    # }

    #list of dictionaries
    students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrir"},
        {"name": "Draco", "house": "Slytherin", "patronus": None}
    ]

    # print(students)
    # for student in students:
    #     print(student)

    # for i in range(len(students)):
    #     print(i+1, students[i])

    # for student in students:
    #     print(student, students[student], sep=": ")

    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=", ")

main()