def calculate_grade(marks, highest_marks):
    
    
    if marks < 0 or highest_marks < 0:
        raise ValueError("Marks and highest marks must be positive")

    if marks > highest_marks:
        raise ValueError("Marks cannot be greater than highest marks")   
    
    percentage = (marks / highest_marks) * 100


    if percentage >= 90 and percentage <=100:
        return 'S'
    
    elif percentage >= 80:
        return 'A'
    
    elif percentage >= 70:
        return 'B'
    
    elif percentage >= 60:
        return 'C'
    
    elif percentage >= 50:
        return 'D'
    
    elif percentage >= 40:
        return 'E'
    
    else:
        return 'F'
  

