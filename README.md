****** Simple grade assigner through TDD *****

this grade assigner is a simple program that assigns grade for a mark when you provide that mark and higest mark.
the function calculate_grade(marks, highest_marks) returns a grade(S,A,B,C,D,E and F) based on 
if the mark is greter than or equal to 90% of higest mark, returns S
if the mark is greter than or equal to 80% of higest mark, returns S
if the mark is greter than or equal to 70% of higest mark, returns S
if the mark is greter than or equal to 60% of higest mark, returns S
if the mark is greter than or equal to 50% of higest mark, returns S
if the mark is greter than or equal to 40% of higest mark, returns S
if the mark is less than 40% of higest mark, returns F

here are my test cases:
calculate_grade(90, 100) should return 'S'
calculate_grade(80, 100), should return 'A'
calculate_grade(70, 100), should return 'B'
calculate_grade(60, 100), should return 'C'
calculate_grade(50, 100), should return 'D'
calculate_grade(40, 100), should return 'E'
calculate_grade(0, 100), should return 'F'

calculate_grade(-10, 100) must raise value error(neagative inputs are not allowed)
calculate_grade(110, 100) must raise value error(mark should not be greater than highest mark)
calculate_grade('nonnumericvalue', 100) must raise value error(non numeric inputs are not allowed)
(calculate_grade(89.5, 100), 'A') should work for decimal inputs also

