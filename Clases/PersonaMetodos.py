# clase
class Person:
    # atributo
    edad = ''
    altura = ''
    # constructor
    def __init__(self, edad, altura):
        self.__edad = edad
        self.__altura = altura

    # metodos
    def getEdad(self):
        return self.__edad

    def getAltura(self):
        return self.__altura

    def setEdad(self, edad):
        self.__edad = edad

    def setAltura(self, altura):
        self.__altura = altura

edad = input("Pon la edad de la persona = ")
altura = input("Pon la altura de la persona = ")


PersonaYo = Person(edad,altura)


print("Mi edad es " + PersonaYo.getEdad())
print("Mi altura es " + PersonaYo.getAltura())
