"""Топты басқару модулі."""
from utils import color_text, print_line


class Group:
    """Студенттер тобын басқаруға арналған класс."""

    def __init__(self, group_name: str) -> None:
        self.group_name = group_name
        self.students: list = []

    def add_student(self, student) -> None:
        """Топқа студент қосады."""
        self.students.append(student)
        print(color_text(f" [+] {student.name} сәтті қосылды!", "green"))

    def show_all_students(self) -> None:
        """Тізімді кесте түрінде шығарады."""
        print(f"\n{color_text('ТОП ТІЗІМІ:', 'yellow')} "
              f"{color_text(self.group_name, 'bold')}")
        print_line()
        print(f"| {'Аты-жөні':<15} | {'Жасы':<5} | {'GPA':<5} |")
        print_line()
        for s in self.students:
            print(str(s))
        print_line()