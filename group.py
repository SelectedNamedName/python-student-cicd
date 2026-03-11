from utils import color_text, print_line

class Group:
    """Студенттер тобын басқаруға арналған класс."""

    def __init__(self, group_name):
        """
        Топты инициализациялау.
        :param group_name: Топтың атауы
        """
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        """
        Топқа жаңа студент қосады және хабарлама шығарады.
        :param student: Қосылатын студент объектісі
        """
        self.students.append(student)
        print(color_text(f" [+] {student.name} сәтті қосылды!", "green"))

    def show_all_students(self):
        """Топтағы барлық студенттердің тізімін кесте түрінде шығарады."""
        print(f"\n{color_text('ТОП ТІЗІМІ:', 'yellow')} {color_text(self.group_name, 'bold')}")
        print_line()
        print(f"| {'Аты-жөні':<15} | {'Жасы':<5} | {'GPA':<5} |")
        print_line()
        for s in self.students:
            print(str(s))
        print_line()