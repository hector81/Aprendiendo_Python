# 3. Cree una clase llamada Persona. Contendrá el nombre, DNI, dirección,
# teléfono y e-mail (este último opcional) de un individuo. Por método
# tendrá mostrar que imprimirá por pantalla los datos de la persona.
#  Utilice esa clase para crear una lista de personas y mostrar cada una
# de ellas. Los datos de cada persona están en el fichero . El formato
# de este fichero es una linea con los datos de cada persona.
# Están separados por ';'. Contiene información por este
# orden: nombre;DNI;dirección;teléfono;e-mail;saldo


# clase
class Persona:
    # atributo
    nombre = ""
    dni = ""
    direccion = ""
    telefono = ""
    email = ""
    saldo = 0.0

    # constructor
    def __init__(self, nombre, dni, direccion, telefono, email, saldo):
        self.__nombre = nombre
        self.__dni = dni
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__saldo = saldo
    # metodos
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDni(self):
        return self.__dni

    def setDni(self, dni):
        self.__dni = dni

    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getsaldo(self):
        return self.__saldo

    def setSaldo(self, saldo):
        self.__saldo = saldo


# metodos
def CrearListaPersonas(ruta):
    listaPersonas = []
    with open(ruta, "r", encoding="utf8") as archivo:
        for linea in archivo.readlines():
            if len(linea) > 1:
                persona = linea.split(";")
                # CREAMOS UNA NUEVA PERSONA Y LA AÑADIMOS A LA LISTA
                nuevaPersona = Persona(persona[0], persona[1], persona[2], persona[3], persona[4], persona[5])
                listaPersonas.append(nuevaPersona)
    return listaPersonas

def leerListaPersonas(listaPersonas):
    for i in range(len(listaPersonas)):
        persona = listaPersonas[i]
        print("PERSONA NÚMERO " + str(i+1))
        print("El nombre de la persona es " + persona.getNombre())
        print("El DNI de la persona es " + persona.getDni())
        print("la dirección de la persona es " + persona.getDireccion())
        print("El teléfono de la persona es " + persona.getTelefono())
        print("El email de la persona es " + persona.getEmail())
        print("El saldo de la persona es " + persona.getsaldo())
        print("*************************************************")
# variables
ruta = "Ejercicio3_Lista_Personas.txt"
# operaciones
listaPersonas = CrearListaPersonas(ruta)
leerListaPersonas(listaPersonas)
