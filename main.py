from services.validators import *


def main():
    patient = {
        "Name:": validate_name(input("Insira seu nome: ")),
        "Age:": input("Insira seu idade: "),
        "Height:": input("Insira sua altura: "),
        "Weight:": input("Insira o seu peso: "),
        "Biologic Gender:": input("Insira o seu genero biologico: ")
    }

main()