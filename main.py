"""
Student Record Management System
Main Program
"""

from file_manager import load_students, save_students
from student import Student
from utils import display_students

students = load_students()


def add_student():
    """Add a new student."""

    print("\n===== Add Student =====")

    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")

    # Check duplicate roll number
    for student in students:
        if student.roll_number == roll_number:
            print("\nA student with this roll number already exists!")
            return

    marks = {}

    while True:

        subject = input("Enter subject name (or 'done' to finish): ")

        if subject.lower() == "done":
            break

        try:
            mark = float(input(f"Enter marks for {subject}: "))
            marks[subject] = mark

        except ValueError:
            print("Invalid marks. Please enter a number.")

    student = Student(name, roll_number, marks)

    students.append(student)

    save_students(students)

    print("\nStudent added successfully!\n")


def view_all_students():
    """Display all students."""
    display_students(students)


def view_student():
    """View a single student."""

    roll_number = input("Enter roll number: ")

    for student in students:

        if student.roll_number == roll_number:

            print("\n===== Student Details =====")
            print(f"Name: {student.name}")
            print(f"Roll Number: {student.roll_number}")
            print(f"Marks: {student.marks}")
            print(f"Total: {student.calculate_total()}")
            print(f"Average: {student.calculate_average():.2f}")
            print(f"Grade: {student.calculate_grade()}")

            return

    print("Student not found.")


def search_student():
    """Search student by name."""

    name = input("Enter student name: ").strip().lower()

    found = False

    for student in students:

        if student.name.lower() == name:

            print("\n===== Student Found =====")
            print(f"Name: {student.name}")
            print(f"Roll Number: {student.roll_number}")
            print(f"Marks: {student.marks}")
            print(f"Total: {student.calculate_total()}")
            print(f"Average: {student.calculate_average():.2f}")
            print(f"Grade: {student.calculate_grade()}")

            found = True
            break

    if not found:
        print("Student not found.")


def sort_students():
    """Display students sorted by average marks."""

    sorted_students = sorted(
        students,
        key=lambda student: student.calculate_average(),
        reverse=True
    )

    display_students(sorted_students)


def update_marks():
    """Update student marks."""

    roll_number = input("Enter roll number: ")

    for student in students:

        if student.roll_number == roll_number:

            subject = input("Enter subject: ")

            try:

                marks = float(input("Enter new marks: "))

                student.marks[subject] = marks

                save_students(students)

                print("Marks updated successfully.")

            except ValueError:
                print("Invalid marks.")

            return

    print("Student not found.")


def delete_student():
    """Delete a student."""

    roll_number = input("Enter roll number: ")

    for student in students:

        if student.roll_number == roll_number:

            students.remove(student)

            save_students(students)

            print("Student deleted successfully.")

            return

    print("Student not found.")


def menu():
    """Display the main menu."""

    while True:

        print("\n========== Student Record Management System ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View One Student")
        print("4. Search Student")
        print("5. Sort Students by Average")
        print("6. Update Marks")
        print("7. Delete Student")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_all_students()

        elif choice == "3":
            view_student()

        elif choice == "4":
            search_student()

        elif choice == "5":
            sort_students()

        elif choice == "6":
            update_marks()

        elif choice == "7":
            delete_student()

        elif choice == "8":
            print("\nThank you for using the Student Record Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()