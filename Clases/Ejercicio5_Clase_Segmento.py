# 5. Cree una clase llamada Segmento. Sus atributos serán dos objetos de
# la clase Punto. Esos puntos tendrán el mismo origen de coordenadas.
# Como método tendrá longitud, que devolverá la distancia entre los dos
# puntos que componen el segmento. Ejecute un programa que cree un segmento,
#  muestre la longitud de ese segmento y el punto más cercano al origen.
# NOTA: Si se reutiliza código ya hecho, este ejercicio se realiza en 20 lineas
#  de código
import math
from Ejercicio4_Clase_Punto import Punto
# clase
class Segmento:
    # atributo

    # constructor
    def __init__(self, x, y, x0=0, y0=0):
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.punto1 = Punto (x, y)
        self.punto2 = Punto (x0, y0)
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

    def getPunto1(self):
        return self.__punto1

    def setPunto1(self, punto1):
        self.__punto1 = punto1

    def getPunto2(self):
        return self.__punto2

    def setPunto2(self, punto2):
        self.__punto2 = punto2

    # método tendrá longitud, que devolverá la distancia entre los dos puntos que componen el segmentO
    def longitud(self):
        longitud = math.sqrt((self.punto1.x - self.punto2.x) ** 2 + (self.punto1.y - self.punto2.y) ** 2)
        print(f'Longitud del segmento = {longitud}')

    # metodo para saber el punto más cercano al origen
    def punto_mas_cercano(self):
        if self.punto1.distancia() > self.punto2.distancia():
            print(f'El punto 2 es el mas cercano al origen con las coordenadas')
            self.punto2.muestra_punto()
        else:
            print(f'El punto 1 es el mas cercano al origen con las coordenadas')
            self.punto1.muestra_punto()

#variables
segmento1 = Segmento(12,7,6,7)
#operaciones
segmento1.longitud()
segmento1.punto_mas_cercano()
