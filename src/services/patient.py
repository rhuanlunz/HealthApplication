from models.Patient import Patient
from utils.console_utils import clear_console
from services.handles import (
    handle_name,
    handle_birthdate,
    handle_height,
    handle_weight,
    handle_biologic_gender,
    handle_patient_id,
)

from repositories.patient_repository import (
    register_patient, 
    select_all_patients,
    select_all_patients_simplificate, 
    select_patient_by_id,
    delete_patient,
    update_patient_name,
    update_patient_birthdate,
    update_patient_height,
    update_patient_weight,
    update_patient_biologic_gender
)

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


def edit_patient_name(patient_id):
    new_name = handle_name()
    update_patient_name(patient_id, new_name)

def edit_patient_birthdate(patient_id):
    new_birthdate = handle_birthdate()
    update_patient_birthdate(patient_id, new_birthdate)

def edit_patient_height(patient_id):
    new_height = handle_height()
    update_patient_height(patient_id, new_height)

def edit_patient_weight(patient_id):
    new_weight = handle_weight()
    update_patient_weight(patient_id, new_weight)

def edit_patient_biologic_gender(patient_id):
    new_biologic_gender = handle_biologic_gender()
    update_patient_biologic_gender(patient_id, new_biologic_gender)
