from datetime import datetime

from services.calcules import calculate_bmr, calculate_imc

class Patient:
    def __init__(self, name = '', birthdate = '01/01/2001', height = 0.0, weight = 0.0, biologic_gender = 'M'):
        self.name: str = name
        self.birthdate: datetime = birthdate
        self.height: float = height
        self.weight: float = weight
        self.biologic_gender: str = biologic_gender
        
        self.imc: float = calculate_imc(height, weight)
        self.bmr: float = calculate_bmr(biologic_gender, height, weight, birthdate)
        self.classification: str = self.classificate_patient()

    def classificate_patient(self):
        if self.imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= self.imc <= 24.9:
            return "Peso normal"
        elif 25 <= self.imc <= 29.9:
            return "Sobrepeso"
        elif 30 <= self.imc <= 34.9:
            return "Obesidade grau I"
        elif 35 <= self.imc <= 39.9:
            return "Obesidade grau II"
        else:
            return "Obesidade grau III"