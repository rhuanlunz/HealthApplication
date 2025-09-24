from services.validators import *
from services.patient import *
from utils.console_utils import *
from utils.functions_utils import *

def show_menu():
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
                clear_console()
                print("- Cadastro de Pacientes - ")
                cad_patient()
                clear_console()
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 2:
            loop = True
            while loop:
                clear_console()
                print("- Listagem de Pacientes - ")
                option = list_patients_menu() 
                if option == 1:
                    list_all_patients()             ##Arrumar o Return dos pacientes listando, ta feio e errado.
                else: 
                    list_especific_patient()
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 3:
            #Remover Pacientes
            pass
        case 4:
            exit()    

def list_patients_menu():
    print("Como voce deseja listar os paciente?")
    print("1 - Listar todos os pacientes.")
    print("2 - Listar paciente especifico.")

    options = [1, 2]
    option = validate_menu_option(options)

    return option