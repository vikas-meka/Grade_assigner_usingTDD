import unittest
from grade_assigner import calculate_grade

class TestGradeCalculator(unittest.TestCase):
    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(80, 100), 'A')
        # self.assertEqual(calculate_grade(90, 100), 'S') 
    
    
 

