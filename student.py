"""Student class for the Student Record Management System."""


class Student:
    """Represents a student."""

    def __init__(self, name, roll_number, marks):
        """Initialize a student object."""
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_total(self):
        """Return the total marks."""
        return sum(self.marks.values())

    def calculate_average(self):
        """Return the average marks."""
        if not self.marks:
            return 0
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        """Return the letter grade."""
        average = self.calculate_average()

        if average >= 90:
            return "A+"
        if average >= 80:
            return "A"
        if average >= 70:
            return "B"
        if average >= 60:
            return "C"
        if average >= 50:
            return "D"
        return "F"

    def to_dict(self):
        """Convert student object into a dictionary."""
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "marks": self.marks
        }