class C(object):
    def __init__(self):
        self._x = None
 
    def getx(self):#Método Get, devuelve el contenido del atriburto x
        return self._x
    def setx(self, value):#Método Set, permite modificar el contenido del atriburto x
        self._x = value
    def delx(self):#Método Del, elimina el contenido del atriburto x
        del self._x


prueba = C()
print(prueba.getx())
prueba.setx(8)
print(prueba.getx())
prueba.delx()
print(prueba.getx())
