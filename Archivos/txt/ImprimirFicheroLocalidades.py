# FUNCIONES
def introducirPalabra():
     while True:
         try:
             palabra = input("Por favor ingrese una palabra: ")
             if palabra != '':
                 print("La palabra es " + palabra)
                 return palabra
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def detectarPalabraEnLinea(provincia,linea):
    boolRep = False
    # recorremos la frase y separamos palabra
    if linea.find(provincia) >= 0:
        boolRep = True
    return boolRep

def introducirNumero():
     while True:
         try:
             numero = int(input("Por favor ingrese el número: "))
             return numero
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def devolverProvincias_PorNumeroCCAA(numero,arrayCCAA_Provincias):
    arrayPROV = []
    # para recorrer las ccaa
    for i in range(len(arrayCCAA_Provincias)):
        if i+1 == numero:
            print('Has elegido ' + str(arrayCCAA_Provincias[i][0]))
            arrayPROV.append(arrayCCAA_Provincias[i][1])

    arrayPROV_total = []
    # para recorrer las provincias
    for i in range(len(arrayPROV)):
        for j in range(len(arrayPROV[i])):
            arrayPROV_total.append(arrayPROV[i][j])
            print(str(j+1) + ' = ' + arrayPROV[i][j])

    return arrayPROV_total

def imprimirMunicipios_PorProvincia(numeroProvincia,arrayProvincias):
    # abrimos el archivo
    archivo_leer = open("ccaamun.txt", encoding="utf8")
    contador = 0
    # por el numero averiguamos el nombre de la provincia
    num = numeroProvincia - 1
    nombreProvincia = ''
    for i in range(len(arrayProvincias)):
        if i == num:
            nombreProvincia = arrayProvincias[i]

    # abrimos archivos de lectura y de escriura
    archivo = 'tabla-de-municipios-de-' + str(nombreProvincia) + '.txt'
    archivo_imprimir = open(archivo, 'w')
    for linea in archivo_leer.readlines():
        # para el encabezado
        if contador == 0:
            archivo_imprimir.write(str(linea) + '\n')
        else: # si detecta que el nombre de provincia está en la línea
            if detectarPalabraEnLinea(nombreProvincia,linea) == True:
                archivo_imprimir.write(str(linea) + '\n')
        contador = contador + 1
    archivo_leer.close()
    archivo_imprimir.close()


# VARIABLES
arrayCCAA_Provincias = [
        ['Andalucía',['Almería','Cádiz','Córdoba','Granada','Huelva','Jaén','Málaga','Sevilla']],
        ['Aragón',['Huesca','Zaragoza','Teruel']],
        ['Canarias',['Las Palmas','Santa Cruz de Tenerife']],
        ['Cantabria',['Cantabria']],
        ['Castilla y León',['Avila','Burgos','León','Palencia','Salamanca','Segovia','Soria','Valladolid','Zamora']],
        ['Castilla-La Mancha',['Albacete','Ciudad Real','Cuenca','Guadalajara','Toledo']],
        ['Cataluña',['Barcelona','Gerona','Lérida','Tarragona']],
        ['Ceuta',['Ceuta']],
        ['Comunidad Valenciana',['Alicante','Castellón','Valencia']],
        ['Comunidad de Madrid',['Madrid']],
        ['Extremadura',['Badajoz','Cáceres']],
        ['Galicia',['La Coruña','Lugo','Orense','Pontevedra']],
        ['Islas Baleares',['Islas Baleares']],
        ['La Rioja',['La Rioja']],
        ['Melilla',['Melilla']],
        ['Navarra',['Navarra']],
        ['País Vasco',['Alava','Guipúzcoa','Vizcaya']],
        ['Principado de Asturias',['Asturias']],
        ['Región de Murcia',['Murcia']]
    ]


# OPERACIONES


print('Elige la CCAA que quieres para ver sus provincias e imprimirlas.')
for i in range(len(arrayCCAA_Provincias)):
        print(str(i+1) + ' = '  + arrayCCAA_Provincias[i][0])

numeroCCAA = introducirNumero()
arrayProvincias = devolverProvincias_PorNumeroCCAA(numeroCCAA,arrayCCAA_Provincias)
print('Ahora introduce el número de provincia para imprimir sus municipios o localidades')
numeroProvincia = introducirNumero()
imprimirMunicipios_PorProvincia(numeroProvincia,arrayProvincias)
