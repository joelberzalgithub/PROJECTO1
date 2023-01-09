# Aqui guardamos las funciones.

# Funcion menu
def menu(menu_, opciones, excepciones=""):
    print(menu_)
    opt = input("\nOpcion: ")
    try:
        if not opt.isdigit():
            if not opt in excepciones:
                raise TypeError("La opcion debe ser un numero.")
        if int(opt) not in opciones:
            if int(opt) not in excepciones:
                raise ValueError("Opcion Invalida.")
        return opt
    except TypeError as error:
        print(error)
        input("Pulsa enter para continuar.")
        return menu(menu_, opciones, excepciones)
