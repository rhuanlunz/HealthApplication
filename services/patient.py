from models.Patient import Patient
from services.handles import *
from database import *
from services.calcules import *
from utils.console_utils import *
from utils.functions_utils import *

def cad_patient():
    clear_console()
    name = handle_name()
    birthdate = handle_birthdate()
    height = handle_height()
    weight = handle_weight()
    biologic_gender = handle_biologic_gender()
    patient = Patient(name, birthdate, height, weight, biologic_gender)
    register_patient(patient)
    
def list_all_patients():
    print(select_all_patients())

def list_all_patient_simplificate():
    print(select_all_patients_simplificate())

def list_especific_patient():
    print(select_patient_by_id(handle_patient_id()))

def delete_patient_by_id():
    delete_patient(handle_patient_id())
