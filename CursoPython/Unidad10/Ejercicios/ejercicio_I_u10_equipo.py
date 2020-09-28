from io import open # importamos el open de io
# creamos lista vacia
personas = []
# creamos diccionario vacio
diccionario_persona = {}
# abrimos y leemos el archivo en la ruta donde se encuentra ubicado con la codificación utf8
archivo = open("Unidad10\\Ejercicios\\equipo.txt","r", encoding="utf8")

# nos podemos asegurar de que el archivo sea legible con readable
if archivo.readable() == True:
    # leemos linea por linea con readlines
    for linea in archivo.readlines():
        # por cada linea creamos un diccionario de persona. Primero separamos datos con split para crear los datos
        lista_linea = linea.split(";")
        # luego asignamos cada fila en una entrada de un diccionario
        diccionario_persona["id"] = lista_linea[0]
        diccionario_persona["nombre"] = lista_linea[1]
        diccionario_persona["apellido"] = lista_linea[2]
        diccionario_persona["nacimiento"] = lista_linea[3]
        # añadimos diccionario a una lista llamada personas.
        personas.append(diccionario_persona)
        #vaciamos diccionario para la siguiente vuelta
        diccionario_persona = {}
    # cerramos archivo para que no de problemas, una vez lo hayamos usado
    archivo.close()

    #Después recorre cada persona de la lista y para cada una muestra la información de todos los campos del
    # diccionario. Los campos del diccionario serán por orden: id, nombre, apellido y nacimiento.
    print(f"Recorremos la lista de personas")
    for i in range(0,len(personas)):
        print(f"PERSONA {i+1} = ")
        # recorremos la posicion de la lista que es un diccionario por clave valor
        for clave in personas[i]:
            print(f"{clave} = {personas[i][clave]}")
            
else: # en caso de que el archivo no sea legible lanzamos un mensaje
    print(f"El archivo tiene un problema y no se puede leer.")


