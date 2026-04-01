"""Вспомогательный модуль для работы с текстом, расчетов и мониторинга."""
import psutil


def color_text(text: str, color: str) -> str:
    """Текстті терминалда түрлі-түсті етіп шығарады."""
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
    """Студенттер тізімінің орташа GPA-ін есептейді."""
    if not students:
        return 0.0
    return sum(s.gpa for s in students) / len(students)


def get_system_stats() -> str:
    """Компьютердің ресурстарын (CPU, RAM) тексеру функциясы."""
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    return f"Мониторинг: CPU: {cpu}%, RAM: {ram}%"


def get_version() -> str:
    """Бағдарламаның ағымдағы нұсқасын қайтарады."""
    return "Версия 1.1 (Logging & Monitoring)"