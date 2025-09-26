def calculate_imc(patient):
    height_meter = patient["Height"] / 100  
    
    IMC = patient["Weight"] / (height_meter ** 2)
    return round(IMC, 2)

def calculate_bmr(patient):
    if patient["Biologic Gender"] == "M":
        BMR = (10 * patient["Weight"]) + (6.25 * patient["Height"]) - (5 * patient["Age"]) + 5
    else:
        BMR = (10 * patient["Weight"]) + (6.25 * patient["Height"]) - (5 * patient["Age"]) - 161

    return round(BMR, 2)
