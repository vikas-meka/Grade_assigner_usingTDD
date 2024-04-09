import unittest
from grade_assigner import calculate_grade

class TestGradeCalculator(unittest.TestCase):
    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(90, 100), 'S') 
        self.assertEqual(calculate_grade(80, 100), 'A')
        self.assertEqual(calculate_grade(70, 100), 'B')
        self.assertEqual(calculate_grade(60, 100), 'C')
        self.assertEqual(calculate_grade(50, 100) , 'D')
    
    
if __name__ == "__main__":
    unittest.main()   

