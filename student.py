"""Студент класы модулі."""


class Student:
    """Студенттің жеке мәліметтерін сақтайтын класс."""

    def __init__(self, name: str, age: int, gpa: float) -> None:
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self) -> str:
        return f"| {self.name:<15} | {self.age:<5} | {self.gpa:<5} |"