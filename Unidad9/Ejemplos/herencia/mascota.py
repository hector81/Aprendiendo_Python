# creamos la clase
class Mascota:
 
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
#----------hasta aquí ya lo teníamos definido-------------