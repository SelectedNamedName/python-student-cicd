class Student:
    """Студенттің жеке мәліметтерін сақтайтын класс."""

    def __init__(self, name, age, gpa):
        """
        Студентті құру.
        :param name: Аты
        :param age: Жасы
        :param gpa: Орташа балл
        """
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        """Студент туралы ақпаратты форматталған жол ретінде қайтарады."""
        return f"| {self.name:<15} | {self.age:<5} | {self.gpa:<5} |"