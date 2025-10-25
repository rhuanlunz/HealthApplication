import sqlite3 as sq

DB_PATH = 'src\data\database\DATABASE.db'

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

