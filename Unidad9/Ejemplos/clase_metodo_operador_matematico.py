class Punto():
    """Clase que va representar un punto en un plano
    Por lo que tendrá una coordenada cartesiana(x,y)
    """
 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, otro):
        """ Devuelve la suma de ambos puntos. """
        return Punto(self.x + otro.x, self.y + otro.y)
    
    def __sub__(self, otro):
        """ Devuelve la resta de ambos puntos. """
        return Punto(self.x - otro.x, self.y - otro.y)


p = Punto(3,4)
q = Punto(2,5)
print(p - q)
print(p + q)