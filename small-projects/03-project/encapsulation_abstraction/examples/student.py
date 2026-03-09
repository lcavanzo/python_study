class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self._student_id = student_id  # Protected attribute(by convention)
        self._grade = grade  # Protected attribute(by convention)

    def get_student_info(self):
        return f"Name: {self.name}, ID: {self._student_id}, Grade: {self._grade}"

    def _update_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self._grade = new_grade
        else:
            print("Invalid grade. Must be between 0 and 100")


# Demonstrating protected access
s = Student("Bob", "S12345", 85)
print(s.get_student_info())

# Accessing protected attribute directly(possible, but discouraged)
print(f"Protected student ID: {s._student_id}")

# Caling protected method directly(possible but discouraged)
s._update_grade(90)
s._update_grade(105)  # still respects internal validation
