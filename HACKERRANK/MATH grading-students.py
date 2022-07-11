def gradingStudents(grades):
    # Write your code here
    arr = []
    
    for grade in grades:
        if (grade < 38):
            arr.append(grade)
        else:
            if (grade % 5 > 2):
                grade += (5 - grade % 5)
            arr.append(grade)
            
    return arr