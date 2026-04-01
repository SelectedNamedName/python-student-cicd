"""Бағдарламаны іске қосу және логиялау модулі."""
import logging
from student import Student
from group import Group
from utils import calculate_average_gpa, color_text, print_line, get_system_stats

# Логиялауды баптау (app.log файлына жазады)
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)


def main():
    """Негізгі функция."""
    logging.info("Бағдарлама іске қосылды.")

    # Тақырып және Мониторинг
    print("\n" + color_text("=== СТУДЕНТТЕРДІ БАСҚАРУ ЖҮЙЕСІ ===", "bold"))
    stats = get_system_stats()
    print(color_text(stats, "blue"))
    logging.info(f"Жүйе күйі: {stats}")

    print_line()

    try:
        # 1. Студенттерді құру
        s1 = Student("Алихан", 20, 3.8)
        s2 = Student("Айгерім", 19, 3.9)
        s3 = Student("Нұрсұлтан", 21, 3.5)
        logging.info(f"Студенттер құрылды: {s1.name}, {s2.name}, {s3.name}")

        # 2. Топ құру
        my_group = Group("IT-24")

        # 3. Студенттерді қосу
        my_group.add_student(s1)
        my_group.add_student(s2)
        my_group.add_student(s3)

        # Ескерту мысалы (GPA төмен болса)
        for s in [s1, s2, s3]:
            if s.gpa < 3.6:
                logging.warning(f"Студенттің үлгерімі төмен: {s.name} (GPA: {s.gpa})")

        # 4. Тізімді шығару
        my_group.show_all_students()

        # 5. Орташа балл
        avg_gpa = calculate_average_gpa(my_group.students)
        result_text = f"Топтың орташа GPA көрсеткіші: {avg_gpa:.2f}"
        print(color_text(result_text, "yellow"))
        logging.info(f"Орташа GPA есептелді: {avg_gpa:.2f}")
        print_line()

    except Exception as e:
        logging.error(f"Күтілмеген қате орын алды: {e}")
        print(color_text("Қате! app.log файлын қараңыз.", "red"))

    logging.info("Бағдарлама жұмысын сәтті аяқтады.")


if __name__ == "__main__":
    main()