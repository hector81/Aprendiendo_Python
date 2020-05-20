# FUNCIONES
def introducirNumero():
     while True:
         try:
             opcion = int(input("Por una opción: "))
             if opcion > 0 and opcion < 6:
                 return opcion
                 break
             else:
                print("Las opciones son del 1 al 5")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")
#####FIN FUNCION

def convertir_capitalize_primera_letra_palabras_lista(lista):
  nuevaLista = []
  palabra = ''
  for i in range(len(lista)):
      palabra = lista[i].capitalize() # convertimos a mayusculas primeras letras
      nuevaLista.append(palabra)
  return nuevaLista
#####FIN FUNCION

def convertir_lower_palabras_lista(lista):
   nuevaLista = []
   palabra = ''
   for i in range(len(lista)):
       palabra = lista[i].lower() # convertimos todo a minusculas
       nuevaLista.append(palabra)
   return nuevaLista
#####FIN FUNCION

def convertirFrases_NotacionCamelCase(fichero):
    with open(fichero) as f:
        for posicion, linea in enumerate(f):
            lineaLista = linea.split(" ")
            lineaListaN = convertir_capitalize_primera_letra_palabras_lista(lineaLista)
            linea_camel_case = ''.join(lineaListaN) # string
            print(f'Línea {posicion}: {linea_camel_case.rstrip()}')
#####FIN FUNCION

def crearFichero_NotacionCamelCase(fichero):
    lineas_fichero_nuevo = ''
    with open(fichero) as f:
        for posicion, linea in enumerate(f):
            lineaLista = linea.split(" ")
            lineaListaN = convertir_capitalize_primera_letra_palabras_lista(lineaLista)
            linea_camel_case = '_'.join(lineaListaN) # string
            lineas_fichero_nuevo = lineas_fichero_nuevo + f'Línea {posicion}: {linea_camel_case.rstrip()}' + "\n"
    with open("LicenseCamelCase.txt", "w") as archivo:
        archivo.writelines([lineas_fichero_nuevo])
#####FIN FUNCION

def convertirFrases_NotacionSnakeCase(fichero):
    with open(fichero) as f:
        for posicion, linea in enumerate(f):
            lineaLista = linea.split(" ")
            lineaListaN = convertir_lower_palabras_lista(lineaLista)
            linea_snake_case = '_'.join(lineaListaN) # string
            print(f'Línea {posicion}: {linea_snake_case.rstrip()}')
#####FIN FUNCION

def crearFichero_NotacionSnakeCase(fichero):
    lineas_fichero_nuevo = ''
    with open(fichero) as f:
        for posicion, linea in enumerate(f):
            lineaLista = linea.split(" ")
            lineaListaN = convertir_lower_palabras_lista(lineaLista)
            linea_snake_case = '_'.join(lineaListaN) # string
            lineas_fichero_nuevo = lineas_fichero_nuevo + f'Línea {posicion}: {linea_snake_case.rstrip()}' + "\n"
    with open("license_snake_case.txt", "w") as archivo:
        archivo.writelines([lineas_fichero_nuevo])
#####FIN FUNCION

def mostrarOpciones():
    print()
    print(f'************ OPCIONES ************')
    print(f'1-CONVERTIR TEXTO LICENCIA A CAMEL CASE')
    print(f'2-CONVERTIR TEXTO LICENCIA A SNAKE CASE')
    print(f'3-GENERAR FICHERO LicenseCamelCase.txt')
    print(f'4-GENERAR FICHERO license_snake_case.txt')
    print(f'5-SALIR')
#####FIN FUNCION

# VARIABLES
fichero = 'license.txt'
salir = False
# OPERACIONES
while salir == False:
    mostrarOpciones()
    opcion = introducirNumero()
    if opcion == 1:
        convertirFrases_NotacionCamelCase(fichero)
    elif opcion == 2:
        convertirFrases_NotacionSnakeCase(fichero)
    elif opcion == 3:
        crearFichero_NotacionCamelCase(fichero)
        print(f'Archivo generado')
    elif opcion == 4:
        crearFichero_NotacionSnakeCase(fichero)
        print(f'Archivo generado')
    elif opcion == 5:
        salir = True
