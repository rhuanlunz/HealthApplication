from services.handles import *
from services.patient import *
from utils.console_utils import *
from utils.functions_utils import *

def show_menu():
    clear_console()
    print("- Menu Principal - ")
    print("1 - Cadastrar Paciente")
    print("2 - Listar Pacientes")
    print("3 - Remover Pacientes")
    print("4 - Sair")

    options = [1,2,3,4]
    option = handle_menu_option(options) 
  
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
                elif option == 3:
                    list_especific_patient()
                elif option == 4:
                    show_menu()
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 3:
            loop = True
            while loop:
                print("- Remover Pacientes - ")
                delete_patient_by_id()
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 4:
            exit()    

def list_patients_menu():
    clear_console()
    print("Como voce deseja listar os paciente?")
    print("1 - Listar todos os pacientes.")
    print("2 - Listar todos os pacientes(SIMPLIFICADO).")
    print("3 - Listar paciente especifico.")
    print("4 - Voltar ao menu principal.")
    
    options = [1, 2, 3, 4]
    option = handle_menu_option(options)

    return option

