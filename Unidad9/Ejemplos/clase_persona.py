# creamos la clase
class Persona:
    # creamos las variables de la clase
    nombre = "Juan"
    Variable_local = 3

    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))

	# creamos la primera funcion
	# para inicializar el atributo nombre
    def inicializar(self, nom):
        self.nombre = nom

	# creamos el segundo método
	# para mostrar el nombre
    def mostrar(self):
        print("Nombre: " , self.nombre)
        print("Edad: ",self.edad)


        