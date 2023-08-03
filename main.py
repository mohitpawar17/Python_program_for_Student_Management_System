students = []

def user_login():
    expected_username = "admin"
    expected_password = "password"

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username == expected_username and password == expected_password:
            print("Login successful.")
            return True
        else:
            print("Invalid credentials. Please try again.")

def add_student(name, roll_number):
    student = {
        "name": name,
        "roll_number": roll_number,
        "attendance": []
    }
    students.append(student)

def display_students():
    if not students:
        print("No students in the system.")
    else:
        print("List of Students:")
        for student in students:
            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Attendance: {student['attendance']}")

def search_student_by_name(name):
    found_students = [student for student in students if student['name'].lower() == name.lower()]
    if not found_students:
        print(f"No student with the name '{name}' found.")
    else:
        print("Found Student(s):")
        for student in found_students:
            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Attendance: {student['attendance']}")

def mark_attendance(name, status):
    found_students = [student for student in students if student['name'].lower() == name.lower()]
    if not found_students:
        print(f"No student with the name '{name}' found.")
    else:
        for student in found_students:
            student['attendance'].append(status)
        print(f"Attendance marked for {name} as {status}")


def main():
    if not user_login():
        return

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Name")
        print("4. Mark Attendance")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter the student's name: ")
            roll_number = input("Enter the student's roll number: ")
            add_student(name, roll_number)
            print("Student added successfully!")

        elif choice == '2':
            display_students()

        elif choice == '3':
            name = input("Enter the name of the student to search: ")
            search_student_by_name(name)

        elif choice == '4':
            name = input("Enter the name of the student to mark attendance: ")
            status = input("Enter attendance status (Present/Absent): ")
            mark_attendance(name, status)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
