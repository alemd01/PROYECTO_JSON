from funciones import leer_json, muestra_rivales, menu, cuenta_local, busca, local_visita, pregunta_divisiones
import time
nba=leer_json("NBA.json")
equipos = muestra_rivales(nba)
while True:
    menu()
    opc = int(input("Introduzca una opcion: "))
    if opc == 1:
        print("Estos son todos los rivales de la temporada")
        for a in range(0,len(equipos)):
            print(equipos[a])
            time.sleep(0.2)
    elif opc == 2:
        contar = cuenta_local(nba)
        print("\nSe ha jugado %i partidos como local." % contar)
    elif opc == 3:
        print("Aqui tienes algunas ciudades con estadio: ")
        print("Boston, Brooklyn, New York City, Philadelphia, Toronto, Atlanta,Charlotte, Miami... ")
        ciudad = input("Introduzca alguna ciudad de EE.UU: ")
        estadio = busca(nba,ciudad)
        print("En la ciudad %s se encuentra el estadio: %s" % (ciudad, estadio[0]))
    elif opc == 4:
        team = input("Introduzca el nombre de un Equipo(Bulls, Heat, Rockets, Lakers...): ")
        locvis = local_visita(team,nba)
        for c in range(0,len(locvis)):
            if locvis[c]:
                resi= "Local"
            else:
                resi= "Visitante"
            print("El partido %i contra el equipo %s se jugo como: %s" % (c,team,resi))
    elif opc == 5:
        print("Las divisiones son: Southwest, Pacific, Northwest, Atlantic, Southeast, Central")
        div = input("Introduzca una division: ")
        equipos5 = pregunta_divisiones(div,nba)
        print("Los equipos de la division %s son: " % div)
        for a in set(equipos5):
            print(a)
    elif opc == 6:
        print("Has elegido la opcion Salir.")
        break
    elif opc >6:
        print("-----------------------------------------")
        print("ERROR HAS INTRODUCIDO UN NUMERO NO VALIDO")
        print("-----------------------------------------")
