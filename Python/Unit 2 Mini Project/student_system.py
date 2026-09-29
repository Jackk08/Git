# Sanjivani University
# Assignment: Student Record Management System
# Author: Vaibhav Nanor

student_database = {}

department_set = set()
subject_set = set()
student_clubs = set()

def add_student(prn, reg_no, dob, name, dept, address, email, subjects_list, marks_list, attendance_list):
    if prn in student_database:
        print(f"Error: Student with PRN {prn} already exists.")
        return

    identity_tuple = (prn, reg_no, dob)
    
    student_database[prn] = {
        "identity": identity_tuple,
        "name": name, 
        "department": dept, 
        "contact": {"address": address, "email": email},
        "subjects": subjects_list, 
        "marks": marks_list, 
        "attendance": attendance_list 
    }
    
    department_set.add(dept)
    for subject in subjects_list:
        subject_set.add(subject)
        
    print(f"Success: Student {name} added to the system.")

def search_student(prn):
    if prn in student_database:
        data = student_database[prn]
        print("\n Student Record Found:")
        print(f"Name: {data['name']}")
        print(f"Identity (PRN, Reg, DOB): {data['identity']}")
        print(f"Department: {data['department']}")
        print(f"Contact: {data['contact']}")
        print(f"Subjects: {data['subjects']}")
        print(f"Marks: {data['marks']}")
        print(f"Attendance: {data['attendance']}")
    else:
        print(f"Error: Student with PRN {prn} not found.")

def update_student(prn, new_marks_list, new_attendance_list):
    if prn in student_database:
        student_database[prn]['marks'] = new_marks_list
        student_database[prn]['attendance'] = new_attendance_list
        print(f"Success: Record for PRN {prn} has been updated.")
    else:
        print(f"Error: Student with PRN {prn} not found.")

def delete_student(prn):
    if prn in student_database:
        del student_database[prn]
        print(f"Success: Record for PRN {prn} has been permanently deleted.")
    else:
        print(f"Error: Student with PRN {prn} not found.")

def calculate_average(prn):
    if prn in student_database:
        marks = student_database[prn]['marks']
        if len(marks) > 0:
            average = sum(marks) / len(marks)
            print(f"Average marks for PRN {prn}: {average:.2f}")
        else:
            print(f"No marks recorded for PRN {prn}.")
    else:
        print(f"Error: Student with PRN {prn} not found.")

def find_highest_scorer():
    if not student_database:
        print("No students in the database.")
        return

    highest_prn = None
    highest_avg = -1
    highest_name = ""

    for prn, data in student_database.items():
        marks = data['marks']
        if len(marks) > 0:
            avg = sum(marks) / len(marks)
            if avg > highest_avg:
                highest_avg = avg
                highest_prn = prn
                highest_name = data['name']
    
    if highest_prn:
        print(f"Highest Scorer: {highest_name} (PRN: {highest_prn}) with an average of {highest_avg:.2f}")
    else:
        print("No valid marks found to calculate a highest scorer.")

def list_by_department(dept_name):
    print(f"\n Students in {dept_name}")
    found = False
    for prn, data in student_database.items():
        if data['department'] == dept_name:
            print(f"- {data['name']} (PRN: {prn})")
            found = True
    if not found:
        print("No students found in this department.")

def count_students():
    total = len(student_database)
    print(f"\nTotal number of students in the system: {total}")

def main():
    while True:
        print("\n Student Record Management System")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Marks/Attendance")
        print("4. Delete Student")
        print("5. Calculate Average")
        print("6. Find Highest Scorer")
        print("7. List Students by Department")
        print("8. Count Total Students")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == '1':
            prn = input("Enter PRN: ")
            reg_no = input("Enter Registration Number: ")
            dob = input("Enter DOB (YYYY-MM-DD): ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            address = input("Enter Address: ")
            email = input("Enter Email: ")
            
            subjects = input("Enter Subjects (comma-separated, e.g., Math,Physics): ").split(',')
            subjects = [s.strip() for s in subjects if s.strip()]
            
            marks = input("Enter Marks (comma-separated, e.g., 85,90): ").split(',')
            marks = [int(m.strip()) for m in marks if m.strip().isdigit()]
            
            attendance = input("Enter Attendance % (comma-separated, e.g., 90,95): ").split(',')
            attendance = [int(a.strip()) for a in attendance if a.strip().isdigit()]
            
            add_student(prn, reg_no, dob, name, dept, address, email, subjects, marks, attendance)
            
        elif choice == '2':
            prn = input("Enter PRN to search: ")
            search_student(prn)
            
        elif choice == '3':
            prn = input("Enter PRN to update: ")
            marks = input("Enter New Marks (comma-separated): ").split(',')
            marks = [int(m.strip()) for m in marks if m.strip().isdigit()]
            
            attendance = input("Enter New Attendance % (comma-separated): ").split(',')
            attendance = [int(a.strip()) for a in attendance if a.strip().isdigit()]
            
            update_student(prn, marks, attendance)
            
        elif choice == '4':
            prn = input("Enter PRN to delete: ")
            delete_student(prn)
            
        elif choice == '5':
            prn = input("Enter PRN to calculate average: ")
            calculate_average(prn)
            
        elif choice == '6':
            find_highest_scorer()
            
        elif choice == '7':
            dept = input("Enter Department Name (e.g., Computer Engineering): ")
            list_by_department(dept)
            
        elif choice == '8':
            count_students()
            
        elif choice == '9':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()