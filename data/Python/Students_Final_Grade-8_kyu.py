# https://www.codewars.com/kata/5ad0d8356165e63c140014d4
# 2023-05-12T12:59:39.048+0000
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    if exam > 75 and projects >= 5:
        return 90
    if exam > 50 and projects >= 2:
        return 75
    return 0