# 4. Cree una clase llamada Punto. Tendrá como atributos las coordenadas x0 e y0 del
# origen (0, 0) por defecto, y las coordenadas x e y del punto en cuestión.
# Los métodos serán: distancia y muestra_punto. El primero devolverá la
# distancia del punto a su origen. El segundo imprimirá por pantalla el
#  mensaje de texto: (x,y), donde x e y son las coordenadas del punto. Ejecute
#  un programa que cree dos puntos con origen en (0,0) y muestre por pantalla
# el que tenga una distancia menor al centro:

#distancia = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)

# Tendremos que importar el modulo math, perteneciente a la librería estándar
#  de Python

import math
# clase
class Punto:
    # atributo

    # constructor
    def __init__(self, x, y, x0=0, y0=0):
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
    # metodos
    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getX0(self):
        return self.__x0

    def setX0(self, x0):
        self.__x0 = x0

    def getY0(self):
        return self.__y0

    def setY0(self, y0):
        self.__y0 = y0

    def distancia(self):
        distancia = math.sqrt((self.x - self.x0) ** 2 + (self.y - self.y0) ** 2)
        return distancia

    def muestra_punto(self):
        print(f'({self.x}, {self.y})')
# metodos
def menorDistanciaDosPuntos(distancia_punto1, distancia_punto2):
    if distancia_punto1 < distancia_punto2:
        print(f'El punto 1 es el que tiene una distancia menor al centro la cual es ' + str(distancia_punto1))
    else:
        print(f'El punto 2 es el que tiene una distancia menor al centro la cual es ' + str(distancia_punto2))
#variables
punto1 = Punto(12,7)
punto2 = Punto(6,7)
#operaciones
print(f'Las coordenadas (x,y) del punto1 son = ')
punto1.muestra_punto()
print(f'Las coordenadas (x,y) del punto2 son = ')
punto2.muestra_punto()
print(f'La distancia del punto1 es = ' + str(punto1.distancia()))
print(f'La distancia del punto2 es = ' + str(punto2.distancia()))
menorDistanciaDosPuntos(punto1.distancia(), punto2.distancia())
