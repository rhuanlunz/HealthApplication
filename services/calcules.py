def calculate_imc(patient):
    IMC =  patient["Weight"] / (patient["Height"] * patient["Height"])
    return IMC

def calculate_bmr(patient):
    pass