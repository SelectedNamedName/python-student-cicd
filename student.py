class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        # Студент ақпаратын әдемі қатар қылып қайтару
        return f"| {self.name:<15} | {self.age:<5} | {self.gpa:<5} |"