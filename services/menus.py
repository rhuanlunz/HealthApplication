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
                print(DATABASE) #debnug apenas
                loop = return_true_false("Deseja continuar(1 - Sim / 2 - Nao): ")
        case 2:
            # Listar Pacientes
            pass
        case 3:
            #Remover Pacientes
            pass
        case 4:
            exit()    
