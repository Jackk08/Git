students = []


def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    prn = input("Enter PRN: ")
    department = input("Enter department: ")
    semester = int(input("Enter semester: "))

    marks = []

    print("\nEnter marks for 5 subjects:")

    for i in range(5):
        mark = float(input("Enter marks for Subject " + str(i + 1) + ": "))
        marks.append(mark)

    attendance = float(input("\nEnter attendance percentage: "))

    average = calculate_average(marks)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "prn": prn,
        "department": department,
        "semester": semester,
        "marks": marks,
        "attendance": attendance,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print("\nStudent record added successfully!")


def display_students():
    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No student records available.")
        return

    for student in students:
        print("Name       :", student["name"])
        print("PRN        :", student["prn"])
        print("Department :", student["department"])
        print("Semester   :", student["semester"])

        print("Subject Marks:")
        for i in range(5):
            print("  Subject", i + 1, ":", student["marks"][i])

        print("Attendance :", student["attendance"], "%")
        print("Average    :", round(student["average"], 2))
        print("Grade      :", student["grade"])


def search_student():
    print("\n Search Student")

    if len(students) == 0:
        print("No student records available.")
        return

    prn = input("Enter PRN to search: ")

    found = False

    for student in students:
        if student["prn"] == prn:
            print("\nStudent Found!")
            print("Name       :", student["name"])
            print("PRN:", student["prn"])
            print("Department :", student["department"])
            print("Semester   :", student["semester"])
            print("Marks      :", student["marks"])
            print("Attendance :", student["attendance"], "%")
            print("Average    :", round(student["average"], 2))
            print("Grade      :", student["grade"])

            found = True
            break

    if found == False:
        print("Student with PRN", prn, "not found.")


def display_grade():
    print("\n Average Marks and Grade")

    if len(students) == 0:
        print("No student records available.")
        return

    prn = input("Enter PRN: ")

    found = False

    for student in students:
        if student["prn"] == prn:

            average = calculate_average(student["marks"])
            grade = calculate_grade(average)

            print("\nStudent Name :", student["name"])
            print("Average Marks:", round(average, 2))
            print("Grade        :", grade)

            found = True
            break

    if found == False:
        print("Student not found.")


while True:

    print(" STUDENT RECORD AND ACADEMIC SYSTEM")

    print("1. Add Student")
    print("2. Display Student Records")
    print("3. Search Student")
    print("4. Calculate Average and Grade")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_grade()

    elif choice == "5":
        print("\nThank you for using the Student Record System.")
        print("Program terminated.")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 5.")