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

    #"hi"


print(contar_pase_y_efectividad())

