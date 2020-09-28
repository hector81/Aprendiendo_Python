# creamos la clase
class Mascota:
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

# Crear objeto
Mascota1 = Mascota()
# Usar métodos
Mascota1.inicializar("Mira")
Mascota1.mostrar()

Mascota2=Mascota()
Mascota2.mostrar()