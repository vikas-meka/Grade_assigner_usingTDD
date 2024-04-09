import unittest
from grade_assigner import calculate_grade

class TestGradeCalculator(unittest.TestCase):

    def test_calculate_grade_highest_marks_minus_ten(self):
        self.assertEqual(calculate_grade(90, 100), 'S')  
    
    def test_calculate_grade_highest_marks_minus_twenty(self):
        self.assertEqual(calculate_grade(80, 100), 'A')
        
