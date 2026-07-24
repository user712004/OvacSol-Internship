"""Utility functions for displaying student records."""

from tabulate import tabulate


def display_students(students):
    """Display all students in a formatted table."""

    if not students:
        print("\nNo student records found.\n")
        return

    table = []

    for student in students:
        table.append([
            student.name,
            student.roll_number,
            student.calculate_total(),
            f"{student.calculate_average():.2f}",
            student.calculate_grade()
        ])

    headers = [
        "Name",
        "Roll No",
        "Total",
        "Average",
        "Grade"
    ]

    print()
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print()