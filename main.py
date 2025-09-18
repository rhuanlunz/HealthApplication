from services.validators import *


def main():
    patient = {
        "Name:": validate_name(),
        "Age:": validate_age(),
        "Height:": validate_height(),
        "Weight:": input("Insira o seu peso: "),
        "Biologic Gender:": input("Insira o seu genero biologico: ")
    }

if __name__ == "__main__":
    main()