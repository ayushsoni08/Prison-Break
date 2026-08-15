import statistics

def main():

    #initialize an empty list of students, this list will be used to store student records entered by the user
    student_records = []

    n = int(input("Enter the number of students: "))

    for _ in range(n):
        student_records.append(add_student())

    #infinite loop only if user selects option 1
    while True:
        print("Enter the operation you want to perform from below options")
        print("1: Add a new student")
        print("2: View Students")
        print("3: Find a student (enter student's name)")
        print("4: Show class Statistics (enter the class number)")
        try:
            option = int(input("Enter opeation to perform: "))
            match option:
                case 1:
                    student_records.append(add_student())

                case 2:
                    print_students(student_records)
                    break

                case 3:
                    student_name = input("Enter student's name to search: ")
                    find_student(student_records, student_name)
                    break

                case 4:
                    class_num = int(input("Enter class number: "))
                    show_class_statistics(student_records, class_num)
                    break

                case _:
                    print("Invalid option.")
                    break
        except ValueError:
            print("Invalid option selected")


def add_student():
 #define the info keys of a student (e.g. name, class, marks)
    student_info = ["name", "class", "marks"]

    student = {}
    for key in student_info:
        match key:
            case "name":
                name = input("Enter student's name: ")
                student[key] = name

            case "class":
                try:
                    class_num = int(input("Enter student's class: "))
                    student[key] = class_num
                except ValueError:
                    print("Invalid input for class")

            case "marks":
                #take 5 subject's marks for each student, assuming user knows the name and number of subjects
                marks = []
                for _ in range(5):
                    try: 
                        mark = int(input("Enter subjects's marks: "))
                        marks.append(mark)

                    except ValueError:
                        print("Invalid input for marks")

                student[key] = marks

            case _:
                continue

    return student


def print_students(students):
    grade = ''
    for student in students:
        highest_marks = max(student["marks"])
        lowest_marks = min(student["marks"])
        total_marks = sum(student["marks"])
        percentage = total_marks/500 * 100
        if percentage >= 90:
            grade = 'A'
        elif percentage >= 80:
            grade = 'B'
        elif percentage >= 70:
            grade = 'C'
        elif percentage >= 60:
            grade = 'D'
        else:
            grade = 'F'

        print(f"Name: {student["name"]}, Class: {student["class"]}, Marks: {student["marks"]}, Highest marks: {highest_marks}, Lowest marks: {lowest_marks}, Percentage: {percentage}, Grade: {grade}")


def find_student(students, name):
    isFound = False

    for student in students:
        if student["name"] == name:
            isFound = True
            print(student)
            break

    if isFound == False:
        print("Student not found.")
        return

def show_class_statistics(students, student_class):
    student_list = []

    for student in students:
        class_statistics = {}
        if student["class"] == student_class:
            class_statistics["name"] = student["name"]
            avg = float(statistics.mean(student["marks"]))
            class_statistics["average"] = avg

            student_list.append(class_statistics)

    num_of_students = len(student_list)
    max_avg = 0.0
    min_avg = 0.0
    student_name_max = ""
    student_name_min = ""

    for student in student_list:
        if student["average"] > max_avg:
            student_name_max = student["name"]
            max_avg = student["average"]

    zero_dic = student_list[0]
    min_avg = zero_dic["average"]
    for student in student_list:
        if student["average"] < min_avg:
            student_name_min = student["name"]
            min_avg = student["average"]

    print(f"Number of students in class {student_class}: {num_of_students}")
    print(f"Student with highest average of marks: {student_name_max}, Average= {max_avg}")
    print(f"Student with lowest average of marks: {student_name_min}, Average= {min_avg}")


main()