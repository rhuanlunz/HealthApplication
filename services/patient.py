from services.validators import *
from database import *
from services.calcules import *

def cad_patient():
    patient = {
            "Name": validate_name(),
            "Age": validate_age(),
            "Height": validate_height(),
            "Weight": validate_weight(),
            "Biologic Gender": validate_biologic_gender(),
        }
    
    patient["IMC"] = calculate_imc(patient)
    patient["BMR"] = calculate_bmr(patient)
    patient["Classification"] = classificate_patient(patient)

    print("Usuario Cadastrado!")
    return DATABASE.append(patient)

def list_all_patients():
    for patient in DATABASE:
                    print(f"Paciente numero {DATABASE.index(patient)}")
                    print(f"NOME: {patient['Name']}")
                    print(f"IDADE:{patient['Age']}")
                    print(f"ALTURA:{patient['Height']}")
                    print(f"PESO:{patient['Weight']}")
                    print(f"GENERO BIOLOGICO:{patient['Biologic Gender']}")

def list_especific_patient():
    #listar paciente baseado no indice nome ou etc.n sei
    pass

def classificate_patient(patient):
    pass