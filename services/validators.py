import re
from database import DATABASE

## Patient infos validations

def validate_name():
    MIN: int = 2 
    MAX: int = 50
    DEFAULT = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s\-]+$'

    while True:
        try:
            name = (input("Insira o nome: ")).strip().title()
        except ValueError:
            print("Insira um nome valido")
        if not re.match(DEFAULT, name):
            print("Nome invalido, tente novamente.")
            continue
        if not (MIN <= len(name) <= MAX):
            print(f"O Nome nao pode ser menor que {MIN} caracteres ou maior que {MAX} caracteres.")
            continue
        
        return name
    
def validate_age():
    MIN: int = 18
    MAX: int = 105

    while True:
        try:
            age: int = int(input("Insira a idade: "))
        except ValueError:
            print("A idade nao pode conter letras.")
            continue

        if not (age > 0):
            print("A idade deve ser positiva.")
            continue
        if not (MIN <= age <= MAX):
            print(f"A sua idade nao pode ser menor que {MIN} anos ou maior que {MAX} anos.")
            continue
        
        return age
    
def validate_height():
    MIN: int = 60
    MAX: int = 220

    while True:
        try:
            height = int(input("Insira o altura(em cm): "))
        except ValueError:
            print("Insira uma altura valida.")
            continue

        if not (MIN <= height <= MAX):
            print(f"A sua idade nao pode ser menor que {MIN}cm ou maior que {MAX}cm.")
            continue 

        return height   
    
def validate_weight():
    MIN: float = 20
    MAX: float = 360

    while True:
        try:
            weight = float(input("Insira o peso: "))
        except ValueError:
            print("Insira um peso valido.")
            continue
        if not (MIN <= weight <= MAX):
            print(f"O seu peso nao pode ser menor que {MIN} Quilos ou maior que {MAX} Quilos.")
            continue

        return weight

def validate_biologic_gender():
    while True:
        biologic_gender = input("Insira seu genero biologico(F/M): ").strip().upper()
        if biologic_gender not in ("F", "M"):
            print("Insira um genero valido.")
            continue

        return biologic_gender    

## Menu Validation

def validate_menu_option(options):
    while True:
        try:
            option = int(input("Insira uma opcao: "))
        except ValueError:
            print("Insira uma opcao valida(Ex: 1).")
            continue

        if not option in options:
            print("Escolha um opcao disponivel.")
            continue

        return option
    
def validate_existing_patient(DATABASE):
    while True:
        try:
            patient_id = int(input("Insira o ID do Paciente: "))
        except ValueError:
            print("Insira um ID valido.")
            continue

        for patient in DATABASE:
            if patient["ID"] == patient_id:
                return patient_id
            
        print("Usuario não encontrado, tente novamente.")
