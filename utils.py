def color_text(text, color):
    # ANSI түстері
    colors = {
        "green": "\033[92m",
        "blue": "\033[94m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "bold": "\033[1m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

def print_line():
    print(color_text("-" * 50, "blue"))

def calculate_average_gpa(students):
    if not students:
        return 0
    return sum(s.gpa for s in students) / len(students)
#пример изменения
def get_version():
    return "Версия 1.1 (Git Lab)"
