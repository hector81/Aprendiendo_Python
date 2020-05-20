import operator
# FUNCIONES
def verAgenda(agenda):
    # ordenamos agenda
    agenda_ordenada = sorted(agenda.items(), key=operator.itemgetter(0))
    for nombre in enumerate(agenda_ordenada):
        print(nombre[1][0] + " = " + agenda[nombre[1][0]])

def devolverAgendaContactos():
    agendaDevolver = {}
    # leemos agenda
    archivo = open("mi_agenda.txt","r")
    for linea in archivo.readlines():
        indiceSeparador = linea.find(" = ")
        nombre = linea[0:indiceSeparador]
        telefono = linea[indiceSeparador + 3:-1]
        agendaDevolver[nombre] = telefono
    archivo.close()
    return agendaDevolver

def imprimirMiAgenda(agenda):
    # ordenamos agenda
    agenda_ordenada = sorted(agenda.items(), key=operator.itemgetter(0))

    with open("mi_agenda.txt", "w") as archivo:
        for nombre in enumerate(agenda_ordenada):
            nombreSTR = str(nombre[1][0])
            telefono = str(agenda[nombre[1][0]])
            archivo.writelines([nombreSTR + " = " + telefono + "\n"])

def introducirNombre():
     while True:
         try:
             nombre = input("Introducir nombre: ")
             if nombre != '':
                 print("El nombre es " + nombre)
                 return nombre
                 break
             else:
                 print("El nombre está vacio ")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def introducirTelefono():
     while True:
         try:
             telefono = input("Introducir telefono: ")
             if telefono != '':
                 if len(telefono) == 9:
                     if telefono[0] == '9' or telefono[0] == '6':
                        print("El telefono es " + telefono)
                        return telefono
                        break
                     else:
                         print("El telefono debe empezar por 9 o por 6 ")
                 else:
                     print("El telefono debe tener nueve números ")
             else:
                 print("El telefono está vacio ")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")



# VARIABLES
agenda = devolverAgendaContactos()
salir = False
permitirRepetidos = False
contador = 0
# OPERACIONES
devolverAgendaContactos()
while (not salir):
    #Pedimos los datos
    nombre = introducirNombre()
    telefono = introducirTelefono()


    while (not permitirRepetidos):
        #Comprobamos si esta dentro del diccionario
        if(nombre not in agenda) and (telefono not in agenda):
            #Añadimos el contacto
            agenda[nombre] = telefono
            print('Añadido el contacto')
            permitirRepetidos = True
        else:
            print('El nombre esta repetido o el telefono esta repetido')
            respuestaPermitirRepetido = input("¿Quieres meterlo aunque haya datos repetidos? (S/N)")
            if(respuestaPermitirRepetido.upper() == "N"):
                permitirRepetidos = True
            else:
                # esto es para que no se repita el nombre en el diccionario
                contador = contador + 1
                strContador = str(contador)
                # si lo que esta repetido es el nombre
                if(nombre in agenda):
                    #Añadimos el contacto
                    nuevoNombre = nombre + " (" + strContador + ")"
                    agenda[nuevoNombre] = telefono
                    print('Añadido el contacto')
                    permitirRepetidos = True
                elif(telefono in agenda):
                    #Añadimos el contacto
                    nuevoTelefono = telefono + " (" + strContador + ")"
                    agenda[nombre] = nuevoTelefono
                    print('Añadido el contacto')
                    permitirRepetidos = True

    permitirRepetidos = False
    #Indicamos si queremos salir
    respuestaSalir = input("¿Quieres meter otro contacto? (S/N)")

    if(respuestaSalir.upper() == "N"):
        salir = True

#Mostramos el diccionario
if salir == True:
    verAgenda(agenda)
    imprimirMiAgenda(agenda)
