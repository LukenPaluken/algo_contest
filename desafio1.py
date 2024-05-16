import random, time
inicio = time.time()

def proceso_pases_aleatorios():
    file = open("pases.txt", 'a')
    jugadoras_australia = [
        ("Claire Colwill", 1),
        ("Ambrosia Malone", 2),
        ("Amy Lawton", 4),
        ("Grace Young", 5),
        ("Alice Arnott", 11),
        ("Kaitlin Nobbs", 15),
        ("Jocelyn Bartram", 19),
        ("Karri Somerville", 20),
        ("Renee Taylor", 21),
        ("Tatum Stewart", 22),
        ("Rebecca Greiner", 29),
        ("Maddison Brooks", 8),
        ("Hattie Shand", 13),
        ("Stephanie Kershaw", 14),
        ("Lucy Sharman", 17),
        ("Jane Claxton", 18),
        ("Grace Stewart", 30),
        ("Zoe Newman", 41)
    ]
    jugadoras_argentina = [
        ("Sofia Toccalino", 2),
        ("Agustina Gorzelany", 3),
        ("Valentina Raposo", 4),
        ("Agostina Alonso", 5),
        ("Agustina Albertarrio", 7),
        ("Maria Granatto", 10),
        ("Clara Barberi", 14),
        ("Rocio Sanchez", 17),
        ("Victoria Sauze", 18),
        ("Eugenia Trinchinetti", 22),
        ("Juana Castellaro", 50),
        ("Cristina Cosentino", 13),
        ("Barbara Dichiara", 16),
        ("Victoria Manuele", 19),
        ("Maria Campoy", 26),
        ("Julieta Jankunas", 28),
        ("Stefania Antoniazzi", 36),
        ("Lara Casas", 61)
    ]

    for i in range(50_000):
        equipo_aleatorio = random.choice(["Argentina", "Australia"])
        jugador_aleatorio = random.choice(jugadoras_argentina if equipo_aleatorio == "Argentina" else jugadoras_australia)
        estado_pase_aleatorio = random.randint(0,1)
        minuto_aleatorio = random.randint(0,60)
     #   lista_cadena = ", ".join(map(str, [equipo_aleatorio, jugador_aleatorio[1], jugador_aleatorio[0], estado_pase_aleatorio, minuto_aleatorio]))
      #  file.write(lista_cadena+"\n")
    file.close()


def leer_registros(nombre_archivo):
    """
    Esta es una función que tiene como parámetro el nombre de un archivo externo, y retorna cada linea de este como una 
    """
    registro = []
    lineas_con_salto = []
    with open(nombre_archivo) as file:
        lineas = file.readlines()
    for linea in lineas: 
        lineas_con_salto = linea.split("\n")
        registro.append(lineas_con_salto[0].split(";"))
    return registro

def contar_pase_y_efectividad ():
    lista = [{'Australia':[]},{'Argentina': []}]

    datos_pases = leer_registros("pases.txt")
    jugadoras_sin_repetir = {}

    for pais, numero_jug, nombre, estado_pase, time in datos_pases:
        if numero_jug not in jugadoras_sin_repetir:
            jugadoras_sin_repetir.update({numero_jug: {'nombre':nombre, 'pais': pais, 'cantidad_pases': 1, 'pases_bien': 0, 'pases_mal': 0, 'porcentaje':0}})
        else:
            jugadoras_sin_repetir[numero_jug]["cantidad_pases"] +=1
        if int(estado_pase) == 1:
            jugadoras_sin_repetir[numero_jug]["pases_bien"] +=1
        else:
            jugadoras_sin_repetir[numero_jug]["pases_mal"] +=1

    for item in jugadoras_sin_repetir:
        jugadoras_sin_repetir[item]["porcentaje"] = round((jugadoras_sin_repetir[item]["pases_bien"] / jugadoras_sin_repetir[item]["cantidad_pases"])*100, 2)
        pais_index = ("Argentina", 1) if jugadoras_sin_repetir[item]["pais"] == "Argentina" else ("Australia", 0)
        lista[pais_index[1]][pais_index[0]].append(
                                                    {
                                                        'numero':item, 
                                                        'nombre':jugadoras_sin_repetir[item]["nombre"], 
                                                        'cantidad_pases': jugadoras_sin_repetir[item]["cantidad_pases"], 
                                                        'pases_bien': jugadoras_sin_repetir[item]["pases_bien"], 
                                                        'pases_mal': jugadoras_sin_repetir[item]["pases_mal"], 
                                                        'porcentaje':jugadoras_sin_repetir[item]["porcentaje"]
                                                    }
                                                  )
        
    lista[1]["Argentina"] = sorted(lista[1]["Argentina"], key=lambda x: x["porcentaje"], reverse=True)
    lista[0]["Australia"] = sorted(lista[0]["Australia"], key=lambda x: x["porcentaje"], reverse=True)
    return lista








proceso_pases_aleatorios()
print(contar_pase_y_efectividad())

fin = time.time()

tiempo_ejecucion = fin-inicio
print(f"El tiempo de ejecucion es: {tiempo_ejecucion:.5f} segundos")