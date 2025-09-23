from services.validators import *

DATABASE = []

def cad_patient():
    patient = {
            "Name": validate_name(),
            "Age": validate_age(),
            "Height": validate_height(),
            "Weight": validate_weight(),
            "Biologic Gender": validate_biologic_gender()
        }
    print("Usuario Cadastrado!")
    return DATABASE.append(patient)

