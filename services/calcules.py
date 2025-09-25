def calculate_imc(patient):
    IMC =  patient["Weight"] / (patient["Height"] * patient["Height"])
    return IMC

def calculate_bmr(patient):
    if patient["Biologic Gender"] == "M":
        BMR = (10 * patient["Weight"]) + (6.25 * patient["Weight"]) -(5 * patient["Age"]) + 5
    else:
        BMR = (10 * patient["Weight"]) + (6.25 * patient["Weight"]) -(5 * patient["Age"]) - 161

    return BMR

