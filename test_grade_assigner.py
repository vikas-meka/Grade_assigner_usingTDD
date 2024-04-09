import unittest
from grade_assigner import calculate_grade

class TestGradeCalculator(unittest.TestCase):

    def test_calculate_grade_highest_marks_minus_ten(self):
        self.assertEqual(calculate_grade(90, 100), 'S')    

    def test_calculate_grade_highest_marks_minus_twenty(self):
        self.assertEqual(calculate_grade(80, 100), 'A')

    def test_calculate_grade_highest_marks_minus_thirty(self):
        self.assertEqual(calculate_grade(70, 100), 'B')    
    
    def test_calculate_grade_highest_marks_minus_forty(self):
        self.assertEqual(calculate_grade(60, 100), 'C')

    def test_calculate_grade_highest_marks_minus_fifty(self):
        self.assertEqual(calculate_grade(50, 100), 'D')

    def test_calculate_grade_highest_marks_minus_sixty(self):
        self.assertEqual(calculate_grade(40, 100), 'E')    

    def test_calculate_grade_lower_bound(self):
        self.assertEqual(calculate_grade(0, 100), 'F')
                
    def test_calculate_grade_negative_marks(self):
        with self.assertRaises(ValueError):
            calculate_grade(-10, 100)

    def test_calculate_grade_non_numeric_marks(self):
        with self.assertRaises(ValueError):
            calculate_grade('abc', 100)

    def test_calculate_grade_marks_greater_than_highest_marks(self):
        with self.assertRaises(ValueError):
            calculate_grade(110, 100)

    def test_calculate_grade_decimal_marks(self):
        self.assertEqual(calculate_grade(89.5, 100), 'A')

    def test_calculate_grade_marks_same_as_highest_marks(self):
        self.assertEqual(calculate_grade(100, 100), 'S')

    def test_calculate_grade_highest_marks_non_integer(self):
        self.assertEqual(calculate_grade(90, 100.0), 'S')

if __name__ == '__main__':
    unittest.main()
