
"""
Вспомогательный модуль для работы с текстом и расчетов.
"""


def color_text(text: str, color: str) -> str:

    """
    Текстті терминалда түрлі-түсті етіп шығарады.

    :param text: Шығарылатын мәтін
    :param color: Түс атауы (green, blue, yellow, red, bold)
    :return: ANSI кодымен форматталған мәтін
    """
    colors: dict[str, str] = {
        "green": "\033[92m",
        "blue": "\033[94m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "bold": "\033[1m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"


def print_line() -> None:
    """Көк түсті бөлу сызығын шығарады."""
    print(color_text("-" * 50, "blue"))


def calculate_average_gpa(students: list) -> float:
    """
    Студенттер тізімінің орташа GPA-ін есептейді.

    :param students: Студенттер объектілерінің тізімі
    :return: Орташа балл (float)
    """
    if not students:
        return 0.0
    return sum(s.gpa for s in students) / len(students)


def get_version() -> str:
    """Бағдарламаның ағымдағы нұсқасын қайтарады."""
    return "Версия 1.1 (Git Lab)"
