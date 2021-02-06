"""https://www.codewars.com/kata/57a429e253ba3381850000fb"""
def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi > 30:
        return 'Obese'
    elif bmi > 25:
        return 'Overweight'
    elif bmi > 18.5:
        return "Normal"
    else:
        return 'Underweight'
