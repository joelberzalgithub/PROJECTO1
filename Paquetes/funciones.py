import os
import random
from Paquetes import datos as d
import sqlite3

# Aqui guardamos las funciones.


def menu(menu_, options, exceptions=""):
    os.system("clear")
    print(menu_)
    opt = input("Option: ".rjust(62))
    try:
        if not opt.isdigit():
            if not opt in exceptions:
                raise TypeError(("=" * 61) + "Invalid Option" + ("=" * 66))
            elif opt.isspace() or opt == "":
                raise TypeError(("=" * 61) + "Invalid Option" + ("=" * 66))
        if opt not in options:
            if opt not in exceptions:
                raise ValueError(("=" * 61) + "Invalid Option" + ("=" * 66))
        return opt
    except TypeError as error:
        print("\n", error)
        input("Press enter to continue".rjust(79))
        return menu(menu_, options, exceptions)
    except ValueError as error:
        print("\n", error)
        input("Press enter to continue".rjust(79))
        return menu(menu_, options, exceptions)


def barajar_mazo(mazo):
    # Se recorre cada posicion del mazo asignandole una nueva posicion a su valor,
    # y intercambiando los valores de ambas posiciones
    for i in range(0, len(mazo) - 1):
        new_pos = random.randint(0, len(mazo) - 1)
        mazo[i], mazo[new_pos] = mazo[new_pos], mazo[i]
    return mazo


def detector_mazo(mazo):
    # Se utiliza esta pequeña funcion para determinar con que mazo estamos trabajando
    if mazo[0] in d.mazo["mazo_default"]:
        return "mazo_default"
    elif mazo[0] in d.mazo["mazo_1"]:
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
            if d.mazo[mazo_opt][d.players[i]["initialCard"]]["priority "] == \
                    d.mazo[mazo_opt][d.players[j]["initialCard"]]["priority "]:
                if d.mazo[mazo_opt][d.players[i]["initialCard"]]["value"] < \
                        d.mazo[mazo_opt][d.players[j]["initialCard"]]["value"]:
                    d.context_game["game"][d.context_game["game"].index(i)], \
                    d.context_game["game"][d.context_game["game"].index(j)] = \
                        d.context_game["game"][d.context_game["game"].index(j)], \
                        d.context_game["game"][d.context_game["game"].index(i)]
            # Si la prioridad de la carta no es la misma, comparamos la prioridad
            else:
                if d.mazo[mazo_opt][d.players[i]["initialCard"]]["priority "] < \
                        d.mazo[mazo_opt][d.players[j]["initialCard"]]["priority "]:
                    d.context_game["game"][d.context_game["game"].index(i)], \
                    d.context_game["game"][d.context_game["game"].index(j)] = \
                        d.context_game["game"][d.context_game["game"].index(j)], \
                        d.context_game["game"][d.context_game["game"].index(i)]
    # Le asignamos a cada jugador su prioridad basada en su posicion en la lista de jugadores
    for i in range(0, len(d.context_game["game"])):
        d.players[d.context_game["game"][i]]["priority"] = len(d.context_game["game"] - 1)
        # El que tiene mas prioridad (primero de la lista) es la banca
        if i == 0:
            d.players[d.context_game["game"][i]]["bank"] = True
        else:
            d.players[d.context_game["game"][i]]["bank"] = False
    # devolvemos la variable
    return mazo


def reset_points():
    # Establecemos en 20 los puntos de todos los jugadores
    for i in d.context_game["game"]:
        d.players[i]["points"] = 20


def check_minimum_2_player_with_points():
    # Establecemos un contador
    count = 0
    # Se recorre la lista de jugadores de la partida actual
    for i in d.context_game["game"]:
        # En caso de que los puntos de un jugador sean mayores a 0, se suma 1 al contador
        if d.players[i]["points"] > 0:
            count += 1
    # En caso de que el contador sea mayor de 1 (minimo 2), se devuelve TRUE, si no se devuelve FALSE
    if count > 1:
        return True
    else:
        return False


def check_conditions():
    try:
        if len(d.context_game["game"]) < 2:
            raise ValueError("Set the players that compose the game first".rjust(97))
        if len(d.mazo) == 0:
            raise ValueError("Set the deck of cards first".rjust(82))
        return
    except ValueError as error:
        print(error)
        input("Press enter to continue".rjust(77))


def create_human_player_name():
    try:
        name = input("Name: ".rjust(45))
        if not name.isspace() or not name == "":
            if not name.isalnum() and not name.isalpha() and not name.isdigit():
                raise TypeError("Incorrect name, please, enter a name not empty with only letters.".rjust(104))
        return name
    except TypeError as error:
        print(error)
        input("Enter to continue".rjust(56))
        return create_human_player_name()

    
def printPlayerStats(id):
    # Creamos un print que imprimirá por pantalla todos los datos del diccionario "players" en función del NIF
    print(
        "name " + str(d.players[id]["name"]) + "\n" +
        "type " + str(d.players[id]["type"]) + "\n" +
        "human " + str(d.players[id]["human"]) + "\n" +
        "bank " + str(d.players[id]["bank"]) + "\n" +
        "initialCard " + str(d.players[id]["initialCard"]) + "\n" +
        "priority " + str(d.players[id]["priority"]) + "\n" +
        "bet " + str(d.players[id]["bet"]) + "\n" +
        "points " + str(d.players[id]["points"]) + "\n" +
        "cards " + str(d.players[id]["cards"]) + "\n" +
        "raoundPoints " + str(d.players[id]["roundPoints"])
    )
    
    
def logToFile(text):
    f = open("logfileSevenAndHalf.txt", "a")
    f.write(text)
    f.close()
    
    
def addRemovePlayers():
    try:
        # Creamos un print que imprimirá por pantalla las opciones del menú
        print("1)New Human Player\n2)New Boot\n3)Show/Remove Players\n4)Go back")
        # Creamos un input que pedirá una de las 4 opciones
        opt = input("Option:\n")
        # Establecemos las condiciones del menú
        if not opt.isdigit():
            raise ValueError("Option must be numeric")
        elif not int(opt) in range(1, 5):
            raise ValueError("Option out of range")
        else:
            return int(opt)
    except ValueError as error:
        print(error)
        input("Press any key to continue\n")
        addRemovePlayers()   
    
    
def settings():
    try:
        # Creamos un print que imprimirá por pantalla las opciones del menú
        print("1)Set Game Players\n2)Set Card's Deck\n3)Set Max Rounds (Default 5 Rounds)\n4)Go back")
        # Creamos un input que pedirá una de las 4 opciones
        opt = input("Option:\n")
        # Establecemos las condiciones del menú
        if not opt.isdigit():
            raise ValueError("Option must be numeric")
        elif not int(opt) in range(1, 5):
            raise ValueError("Option out of range")
        else:
            return int(opt)
    except ValueError as error:
        print(error)
        input("Press any key to continue\n")
        addRemovePlayers()
        
        
def setMaxRounds():
    try:
        maxRounds = input("Rounds of the next game: ")
        if maxRounds.isdigit() and int(maxRounds) in range(1, 31):
            d.context_game.update({"maxRounds": maxRounds})
        elif int(maxRounds) < 1:
            raise ValueError("There can't be less than 1 round")
        elif int(maxRounds) > 30:
            raise ValueError("There can't be more than 30 rounds")
        else:
            raise ValueError("Rounds must be numeric")
    except ValueError as error:
        print(error)
        setMaxRounds()
        
