import random
import datos as d
# Aqui guardamos las funciones.


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


def barajar_mazo(mazo):
    # Se recorre cada posicion del mazo asignandole una nueva posicion a su valor,
    # y intercambiando los valores de ambas posiciones
    for i in range(0, len(mazo) - 1):
        new_pos = random.randint(0, len(mazo) - 1)
        mazo[i], mazo[new_pos] = mazo[new_pos], mazo[i]
    return mazo


def detector_mazo(mazo):
    # Se utiliza esta pequeña funcion para determinar con que mazo estamos trabajando
    if mazo[0] in d.mazos["mazo_default"]:
        return "mazo_default"
    elif mazo[0] in d.mazos["mazo_1"]:
        return "mazo_1"


def set_game_priority(mazo):
    # barajamos el mazo
    mazo = barajar_mazo(mazo)
    # determinamos que mazo estamos usando
    mazo_opt = detector_mazo(mazo)
    # Le asignamos a cada jugador una carta del mazo
    for i in d.context_game["game"]:
        d.players[i]["initialCard"] = mazo[random.randint(0, len(mazo))]
    # Ordenamos la lista de jugadores segun la prioridad de sus cartas
    for i in d.context_game["game"]:
        for j in d.context_game["game"]:
            # Primero se mira si la prioridad de la carta es la misma, en ese caso comparamos el valor de las cartas
            if d.mazos[mazo_opt][d.players[i]["initialCard"]]["priority "] == \
                    d.mazos[mazo_opt][d.players[j]["initialCard"]]["priority "]:
                if d.mazos[mazo_opt][d.players[i]["initialCard"]]["value"] > \
                        d.mazos[mazo_opt][d.players[j]["initialCard"]]["value"]:
                    d.context_game["game"][d.context_game["game"].index(i)], \
                    d.context_game["game"][d.context_game["game"].index(j)] = \
                        d.context_game["game"][d.context_game["game"].index(j)], \
                        d.context_game["game"][d.context_game["game"].index(i)]
            # Si la prioridad de la carta no es la misma, comparamos la prioridad
            else:
                if d.mazos[mazo_opt][d.players[i]["initialCard"]]["priority "] >\
                        d.mazos[mazo_opt][d.players[j]["initialCard"]]["priority "]:
                    d.context_game["game"][d.context_game["game"].index(i)], \
                    d.context_game["game"][d.context_game["game"].index(j)] = \
                        d.context_game["game"][d.context_game["game"].index(j)], \
                        d.context_game["game"][d.context_game["game"].index(i)]
    # Le asignamos a cada jugador su prioridad basada en su posicion en la lista de jugadores
    for i in range (0, len(d.context_game["game"])):
        d.players[d.context_game["game"][i]]["priority"] = i
    # devolvemos la variable
    return mazo


