from services.validators import *
from database import *

def cad_patient():
    patient = {
            "Name": validate_name(),
            "Age": validate_age(),
            "Height": validate_height(),
            "Weight": validate_weight(),
            "Biologic Gender": validate_biologic_gender(),
            "IMC": calculate_imc(patient),
            "BMR": calculate_bmr(),                           #DESCOBRIR MANEIRA DE ADICIONAR OS CALCULOS NO PACIENTE.
            "Classification": classificate_patient()
        }
    print("Usuario Cadastrado!")
    return DATABASE.append(patient)

def list_all_patients():
    for patient in DATABASE:
                    print(f"Paciente numero {DATABASE.index(patient)}")
                    print("NOME:" + patient["Name"])
                    print("IDADE:" + patient["Age"])
                    print("ALTURA:" + patient["Height"])
                    print("PESO:" + patient["Weight"])
                    print("GENERO BIOLOGICO:" + patient["Biologic_gender"])

def list_especific_patient():
    #listar paciente baseado no indice nome ou etc.n sei
    pass





#Remove that file, put on in a new file for more modularization.                    
def calculate_imc(patient):
    IMC =  patient["Weight"] / (patient["Height"] * patient["Height"])
    print(IMC)

def calculate_bmr():
    pass

def classificate_patient():
    pass