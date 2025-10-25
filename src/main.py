from services.menus import show_menu
from data.database import init_database

if __name__ == "__main__":
    init_database()
    show_menu()
    
