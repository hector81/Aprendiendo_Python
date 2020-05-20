def crearArrayMunicipiosEspaña():
    archivo = open("Tabla_Pobla_local 23 09 2019.txt","r")
    arrayMunicipios = []
    arrayLinea = []

    # leemos lineas
    for linea in archivo.readlines():
        # recorremos la linea y separamos palabras y las metemos en array
        for palabra in linea.split():
            # hacemos un array por linea
            arrayLinea.append(palabra)
        # fin for
        # añadimos arraylinea a array principal
        arrayMunicipios.append(arrayLinea)
        # vaciamos array para siguiente linea
        arrayLinea = []

    return arrayMunicipios
    # cerramos
    archivo.close()

def buscarMunicipiosPorCodigoPosta(codigoPostal):
    arrayMunicipios = crearArrayMunicipiosEspaña()
    arrayDatos = []

    for i in range(len(arrayMunicipios)):
        for j in range(len(arrayMunicipios[i])):
            # la posicion 1 es porque el primero es el codigo codigoPostal
            if arrayMunicipios[i][j] == codigoPostal:
                arrayDatos = arrayMunicipios[i]

    # leemos
    resultado = ''
    for x in range(len(arrayDatos)):
            resultado = str(arrayDatos[3])

    print(resultado)



def introducirCodigoPostal():
     while True:
         try:
             codigo = input("Por favor ingrese un codigo postal: ")
             if codigo != '':
                 return codigo
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


codigoPostal = introducirCodigoPostal()
buscarMunicipiosPorCodigoPosta(codigoPostal)
