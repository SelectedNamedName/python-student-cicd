import unittest
from student import Student
from utils import calculate_average_gpa

class TestStudentSystem(unittest.TestCase):

    def test_student_creation(self):
        """Тест: правильно ли создается объект студента"""
        s = Student("Test User", 20, 3.5)
        self.assertEqual(s.name, "Test User")
        self.assertEqual(s.age, 20)
        self.assertEqual(s.gpa, 3.5)

    def test_calculate_average_gpa(self):
        """Тест: корректно ли считается средний балл"""
        students = [
            Student("A", 20, 3.0),
            Student("B", 21, 4.0)
        ]
        avg = calculate_average_gpa(students)
        self.assertEqual(avg, 3.5)

    def test_calculate_average_empty(self):
        """Тест: что будет, если список студентов пуст"""
        avg = calculate_average_gpa([])
        self.assertEqual(avg, 0)

if __name__ == '__main__':
    unittest.main()