from services.validators import *
from services.patient import *
from utils.console_utils import *
from utils.functions_utils import *

def show_menu():
    clear_console()
    print("- Menu Principal - ")
    print("1 - Cadastras Paciente")
    print("2 - Listar Pacientes")
    print("3 - Remover Pacientes")
    print("4 - Sair")

    options = [1,2,3,4]
    option = validate_menu_option(options) 
  
    match option:
        case 1: 
            loop = True
            while loop:
                print("- Cadastro de Pacientes - ")
                cad_patient()
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 2:
            loop = True
            while loop:
                print("- Listagem de Pacientes - ")
                option = list_patients_menu() 
                if option == 1:
                    list_all_patients()
                elif option == 2:
                    list_all_patient_simplificate()
                else:
                    list_especific_patient()
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 3:
            loop = True
            while loop:
                print("- Remover Pacientes - ")
                remove_patient_by_id()
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 4:
            exit()    

def list_patients_menu():
    clear_console()
    print("Como voce deseja listar os paciente?")
    print("1 - Listar todos os pacientes.")
    print("2 - Listar todos os pacientes(SIMPLIFICADO).")
    print("2 - Listar paciente especifico.")
    

    options = [1, 2, 3]
    option = validate_menu_option(options)

    return option

