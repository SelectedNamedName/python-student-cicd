from student import Student
from group import Group
from utils import calculate_average_gpa, color_text, print_line

def main():
    # Басты тақырып
    print("\n" + color_text("=== СТУДЕНТТЕРДІ БАСҚАРУ ЖҮЙЕСІ ===", "bold"))
    print_line()

    # 1. Студенттерді құру
    s1 = Student("Алихан", 20, 3.8)
    s2 = Student("Айгерім", 19, 3.9)
    s3 = Student("Нұрсұлтан", 21, 3.5)

    # 2. Топ құру
    my_group = Group("IT-24")

    # 3. Студенттерді қосу
    my_group.add_student(s1)
    my_group.add_student(s2)
    my_group.add_student(s3)

    # 4. Тізімді шығару
    my_group.show_all_students()

    # 5. Орташа балл (Қате жөнделді: .2f)
    avg_gpa = calculate_average_gpa(my_group.students)
    result_text = f"Топтың орташа GPA көрсеткіші: {avg_gpa:.2f}"
    print(color_text(result_text, "yellow"))
    print_line()

if __name__ == "__main__":
    main()