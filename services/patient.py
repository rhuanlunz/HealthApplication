from services.validators import *
from database import *
from services.calcules import *
from utils.console_utils import *
from utils.functions_utils import *

def cad_patient():
    clear_console()
    patient = {
            "ID": len(DATABASE) + 1,
            "Name": validate_name(),
            "Age": validate_age(),
            "Height": validate_height(),
            "Weight": validate_weight(),
            "Biologic Gender": validate_biologic_gender(),
        }
    
    patient["IMC"] = calculate_imc(patient)
    patient["BMR"] = calculate_bmr(patient)
    patient["Classification"] = classificate_patient(patient)

    print(f"Usuario Cadastrado com sucesso no ID {patient["ID"]}")
    return DATABASE.append(patient)

def list_all_patients():
    clear_console()
    for patient in DATABASE:
        print(f"--- Paciente ID {patient["ID"]} --")
        print(f"NOME: {patient['Name']}")
        print(f"IDADE:{patient['Age']}")
        print(f"ALTURA:{patient['Height']}")
        print(f"PESO:{patient['Weight']}")
        print(f"GENERO BIOLOGICO:{patient['Biologic Gender']}")
        print(f"IMC:{patient['IMC']}")
        print(f"TMB:{patient['BMR']}")
        print(f"Classificacao:{patient['Classification']}")
        print("-----------------------------------")

def list_all_patient_simplificate():
    clear_console()
    for patient in DATABASE:
        print(f"--- Paciente ID {patient["ID"]} --")
        print(f"NOME: {patient['Name']}")
        print("-----------------------------------")

def list_especific_patient():
    print("espeficio")

def classificate_patient(patient):
    imc = patient["IMC"]

    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 34.9:
        return "Obesidade grau I"
    elif 35 <= imc <= 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def delete_patient_by_id():
    ##Delete patient
    pass