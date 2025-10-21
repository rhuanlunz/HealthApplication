from services.handles import *
from database import *
from services.calcules import *
from utils.console_utils import *
from utils.functions_utils import *

def cad_patient():
    clear_console()
    patient = {
            "Name": handle_name(),
            "Birthdate": handle_birthdate(),
            "Height": handle_height(),
            "Weight": handle_weight(),
            "Biologic Gender": handle_biologic_gender(),
        }
    patient["IMC"] = calculate_imc(patient)
    patient["BMR"] = calculate_bmr(patient)
    patient["Classification"] = classificate_patient(patient)
    register_patient(patient)
    
def list_all_patients():
    print(select_all_patients())

def list_all_patient_simplificate():
    print(select_all_patients_simplificate())

def list_especific_patient():
    print(select_patient_by_id(handle_patient_id()))

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
    delete_patient(handle_patient_id())
