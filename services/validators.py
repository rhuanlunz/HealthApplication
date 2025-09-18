import re

def validate_name():
    
    MIN: int = 2 
    MAX: int = 50
    DEFAULT = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s\-]+$'

    while True:
        name = input("Insira o nome: ")
        if not name.strip():
            print("O Nome nao pode ser vazio.")
            continue
        if not (name.isalpha()):
            print("O nome deve conter letras.")
            continue
        if not (MIN <= len(name) <= MAX):
            print(f"O Nome nao pode ser menor que {MIN} caracteres ou maior que {MAX}.")
            continue

        return re.match(DEFAULT, name) is not None
    
def validate_age():
    MIN: int = 18
    MAX: int = 105

    while True:
        try:
            age: int = int(input("Insira a idade: "))
        except ValueError:
            print("A idade nao pode conter letras.") ##Is not validate '.' in age.
            continue
        if not (MIN <= age <= MAX):
            print(f"A sua idade nao pode ser menor que {MIN} anos ou maior que {MAX}.")
            continue
        
        return age
    
##Colocar altura em centimentro...melhor
def validate_height():
    MIN: float = 0.60
    MAX: float = 2.20

    while True:
        try:
            height = float(input("Insira o altura: "))
        except ValueError:
            print("Insira uma altura valida.")
            continue
        if not (MIN <= height <= MAX):
            print(f"O seu peso nao pode ser menor que {MIN} centimentros ou maior que {MAX}.")
            continue 

        return height   


##Terminar de validar.
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
            print(f"O seu peso nao pode ser menor que {MIN} anos ou maior que {MAX}.")
            continue 

