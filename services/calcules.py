from datetime import date

def calc_age(birthdate):
    TODAY = date.today()
    age = TODAY.year - birthdate.year
    if (TODAY.month, TODAY.day) < (birthdate.month, birthdate.day) :
        age -= 1
    return age

def calculate_imc(height, weight):
    height_meter = height / 100  
    
    IMC = weight / (height_meter ** 2)
    return round(IMC, 2)

def calculate_bmr(biologic_gender, height, weight, birthdate):
    if biologic_gender == "M":
        BMR = (10 * weight) + (6.25 * height) - (5 * calc_age(birthdate)) + 5
    else:
        BMR = (10 * weight) + (6.25 * height) - (5 * calc_age(birthdate)) - 161

    return round(BMR, 2)
