from services.validators import *
from database import *
from services.calcules import *
from utils.console_utils import *

def cad_patient():
    clear_console()
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
    clear_console()
    for patient in DATABASE:
                    print(f"--- Paciente numero {DATABASE.index(patient)} --")
                    print(f"NOME: {patient['Name']}")
                    print(f"IDADE:{patient['Age']}")
                    print(f"ALTURA:{patient['Height']}")
                    print(f"PESO:{patient['Weight']}")
                    print(f"GENERO BIOLOGICO:{patient['Biologic Gender']}")
                    print("-------------------------------------------------")

def list_especific_patient():
    #listar paciente baseado no indice nome ou etc.n sei
    pass

def classificate_patient(patient):
    pass

##ta ficando na memoria quando da um input errado e cancela o programa.