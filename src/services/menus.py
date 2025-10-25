from utils.console_utils import clear_console
from utils.functions_utils import return_true_false
from services.handles import (
    handle_menu_option, 
    handle_patient_id
)
from services.patient import cad_patient
from services.patient import (
    list_all_patients,
    list_all_patient_simplificate,
    list_especific_patient,
    delete_patient_by_id,   
    edit_patient_name,
    edit_patient_birthdate,
    edit_patient_height,
    edit_patient_weight,
    edit_patient_biologic_gender     
)

def show_menu():
    clear_console()
    print("- Menu Principal - ")
    print("1 - Cadastrar Paciente")
    print("2 - Listar Pacientes")
    print("3 - Remover Pacientes")
    print("4 - Editar Pacientes")
    print("5 - Sair")

    options = [1,2,3,4]
    option = handle_menu_option(options) 
  
    match option:
        case 1: #CADASTRO
            loop = True
            while loop:
                print("- Cadastro de Pacientes - ")
                cad_patient()
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 2: #LISTAGEM
            loop = True
            while loop:
                print("- Listagem de Pacientes - ")
                option = list_patients_menu() 
                match option:
                    case 1:
                        list_all_patients()
                    case 2:
                        list_all_patient_simplificate()
                    case 3:
                        list_especific_patient()
                    case 4:
                        show_menu()
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 3: #REMOVER 
            loop = True
            while loop:
                print("- Remover Pacientes - ")
                delete_patient_by_id()
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 4: # EDIT
            loop = True 
            while loop:
                print("Escolha o paciente que voce deseja editar")
                list_all_patient_simplificate()
                patient_id = handle_patient_id()
                
                option = edit_patients_menu()

                match option:
                    case 1:
                        edit_patient_name(patient_id) 
                    case 2:
                        edit_patient_birthdate(patient_id)
                    case 3:
                        edit_patient_height(patient_id)
                    case 4:
                        edit_patient_weight(patient_id)
                    case 5:
                        edit_patient_biologic_gender(patient_id)
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
            show_menu()
        case 5: # SAIR
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

def edit_patients_menu():
    clear_console()

    print("Escolha oque voce deseja editar!")
    print("1 - Editar nome do paciente.")
    print("2 - Editar data de nascimento do paciente.")
    print("3 - Editar altura do paciente.")
    print("4 - Editar peso do paciente.")
    print("5 - Editar genero biologico do paciente.")

    options = [1, 2, 3, 4, 5]
    option = handle_menu_option(options)

    return option
