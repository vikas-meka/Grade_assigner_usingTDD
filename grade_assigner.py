def calculate_grade(marks, highest_marks):
    
    
    percentage = (marks / highest_marks) * 100


    if percentage >= 90 and percentage <=100:
        return 'S'
    
    elif percentage >= 80:
        return 'A'
    
    elif percentage >= 70:
        return 'B'
  

