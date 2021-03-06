import json
import sys
def leer_json(fichero):
    try:
        with open(fichero) as f:
            datos=json.load(f)
            return datos
    except:
        print("ERROR AL LEER EL FICHERO")
        sys.exit(0)

def menu():
    print("---------EJERCICIO_JSON_NBA---------\n")
    print("  1. Muestra todos los rivales.")
    print("  2. Cuenta las veces que se jugo de local en toda la temporada.")
    print("  3. Buscar el nombre del estadio preguntando por la ciudad en la que se encuentre este.")
    print("  4. Pedir por teclado el nombre de un equipo y devuelve si juega como local o visitante.")
    print("  5. Preguntar por una division y que devuelva los equipos perteneciente a esta.")
    print("  6. Salir")
    print("\n------------------------------------")
def muestra_rivales(a):
    equipos=[]
    for equipo in a["schedule"]:
        equipos.append(equipo["opponent"]["nickname"])
    return equipos
def cuenta_local(nba):
    listita=[]
    cont=0
    cont2=0
    for equipo in nba["schedule"]:
        listita.append(equipo["isHomeGame"])
        if listita[cont] == True:
            cont2=cont2+1
        cont=cont+1
    return cont2
def busca(nba,ciudad):
    estadios=[]
    for estadio in nba.get("schedule"):
        if estadio.get("where").get("city") == ciudad:
            estadios.append((estadio.get("where").get("arena")))
    return estadios
def local_visita(equipo,nba):
    listinha=[]
    for equipin in nba.get("schedule"):
        if equipin.get("opponent").get("nickname") == equipo:
            listinha.append((equipin.get("isHomeGame")))
    return listinha
def pregunta_divisiones(div,nba):
    equipetes = []
    for equipete in nba.get("schedule"):
        if equipete.get("opponent").get("division") == div:
            equipetes.append((equipete.get("opponent").get("nickname")))
    return equipetes
