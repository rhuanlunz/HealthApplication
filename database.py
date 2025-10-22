import sqlite3 as sq

from models.Patient import Patient

DB_PATH = 'DATABASE.db'

def init_database():
    with sq.connect(DB_PATH) as CONNECT:
        CURSOR = CONNECT.cursor()
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS PATIENTS(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME VARCHAR NOT NULL,
                    BIRTHDATE TEXT NOT NULL,
                    HEIGHT REAL NOT NULL,
                    WEIGHT REAL NOT NULL,
                    BIOLOGICAL_GENDER CHAR NOT NULL,
                    IMC REAL,
                    BMR REAL,
                    CLASSIFICATION TEXT
                )
            ''')

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



