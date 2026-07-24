"""Handles saving and loading student data."""

import json
import os
from student import Student

FILE_NAME = "students.json"


def load_students():
    """Load students from the JSON file."""

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        students = []

        for item in data:
            student = Student(
                item["name"],
                item["roll_number"],
                item["marks"]
            )
            students.append(student)

        return students

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_students(students):
    """Save students to the JSON file."""

    data = []

    for student in students:
        data.append(student.to_dict())

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)