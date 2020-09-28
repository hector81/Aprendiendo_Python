class punto():
    """Clase que va representar un punto en un plano
    Por lo que tendrá una coordenada cartesiana(x,y)
    """
 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def __str__(self):
    """ Muestra un par de variables como una tupla, el punto cartesiano"""
    return "(" + str(self.x) + ", " + str(self.y) + ")"

p = punto(7,15)
str(p)
print(p)
print(str(p))