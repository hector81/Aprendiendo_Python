# 2. Cree una clase llamada Fichero. Esa clase tendrá un atributo llamado ruta
#  y otro llamado texto. Implemente dos métodos: leer_fichero, que leerá el
# fichero dado por el atributo ruta y guardará su contenido en el atributo
# texto. mostrar_fichero, que imprimirá por pantalla el texto del fichero
# leído. Use su nueva clase para leer el fichero que contiene al ejercicio 1.


# clase
class Fichero:
    # atributo
    ruta = ""
    texto = ""

    # constructor
    def __init__(self, ruta, texto):
        self.__ruta = ruta
        self.__texto = texto

    # metodos
    def getRuta(self):
        return self.__ruta

    def setRuta(self, ruta):
        self.__ruta = ruta

    def getTexto(self):
        return self.__texto

    def setTexto(self, texto):
        self.__texto = texto

    def leer_fichero(self, ruta):
        with open(ruta, "r", encoding="utf8") as archivo:
            linea = archivo.readline()
            self.__texto += linea

    def mostrar_fichero(self):
        print(self.__texto)  # para leer el texto


ruta = "Ejercicio1.txt"
texto = ""
miFichero = Fichero(ruta, texto)
miFichero.leer_fichero(ruta)
miFichero.mostrar_fichero()
