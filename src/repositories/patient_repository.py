import _sqlite3 as sq
from models.Patient import Patient
from data.database import DB_PATH

def register_patient(patient: Patient):
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute('''
           INSERT INTO
                PATIENTS
                       (NAME, BIRTHDATE, HEIGHT, WEIGHT, BIOLOGICAL_GENDER, IMC, BMR, CLASSIFICATION)
                VALUES
                       (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
            (patient.name, patient.birthdate, patient.height, patient.weight, patient.biologic_gender, patient.imc, patient.bmr, patient.classification)
        )

def select_all_patients():
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute('''
           SELECT * FROM PATIENTS
        ''')
        return CURSOR.fetchall()
    
def select_all_patients_simplificate():
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute('''
           SELECT ID, NAME FROM PATIENTS
        ''')
        return CURSOR.fetchall()

def select_patient_by_id(id):
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute('''
           SELECT * FROM PATIENTS WHERE id = ?
        ''', (id,))
        return CURSOR.fetchall()

def delete_patient(id):
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute('''
           DELETE FROM PATIENTS WHERE id = ?
        ''', (id,))

def update_patient_name(patient_id, new_name):
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute(''' 
            UPDATE PATIENTS SET NAME = ? WHERE ID = ?
        ''', (new_name, patient_id))


def update_patient_birthdate(patient_id, new_birthdate):
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute(''' 
            UPDATE PATIENTS SET BIRTHDATE = ? WHERE ID = ?
        ''', (new_birthdate, patient_id))


def update_patient_height(patient_id, new_height):
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute(''' 
            UPDATE PATIENTS SET HEIGHT = ? WHERE ID = ?
        ''', (new_height, patient_id))


def update_patient_weight(patient_id, new_weight):
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute(''' 
            UPDATE PATIENTS SET WEIGHT = ? WHERE ID = ?
        ''', (new_weight, patient_id))

def update_patient_biologic_gender(patient_id, new_biologic_gender):
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute(''' 
            UPDATE PATIENTS SET BIOLOGICAL_GENDER = ? WHERE ID = ?
        ''', (new_biologic_gender, patient_id))
