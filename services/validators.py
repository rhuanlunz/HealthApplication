import re

def validate_name(name: str, MIN: int = 2, MAX: int = 50):
    while True:
        if not name.strip():
            print("O Nome nao pode ser vazio.")

        if not (MIN <= len(name) <= MAX):
            print("O Nome nao pode ser menor que 2 caracteres ou maior que 50.")

        DEFAULT = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s\-]+$'    
        return re.match(DEFAULT, name) is not None