def return_true_false(message):
    while True:
        try:
            value = input(message).strip()
        except ValueError:
            print("Opcao Invalida, tente novamente")
            continue

        if value == "1":
            return True
        elif value == "2":
            return False
        else:
            print("Opcao invalida, tente novamente.")
            continue
        

