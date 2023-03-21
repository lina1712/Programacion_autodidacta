import random


def jugar():
    usuario = input("Escoge una opcion: pi = piedra, pa = papel y ti = tijera.\n").lower()
    computadora = random.choice(["pi", "pa", "ti"])

    if usuario == computadora:
        return "¡Empate! la computadora tambien escogio " + computadora

    if gano_el_jugador(usuario, computadora):
        return "¡Ganaste! la computadora escogio " + computadora

    return "¡Perdiste! la computadora escogio " + computadora


def gano_el_jugador(jugador, oponente):
    #Retornar True (verdadero) si gana el juegador
    #Piedra gana a Tijera (pi>ti)
    #Tijera gana a Papel(ti>pa)
    #Papel gana a Piedra(pa>pi)
    if ((jugador == "pi" and oponente =="ti")
        or (jugador == "ti" and oponente == "pi")
        or (jugador =="pa" and oponente=="pi")
        ):
        return True
    else:
        return False


print (jugar())
    
