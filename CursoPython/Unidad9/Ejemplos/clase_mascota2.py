# creamos la clase
class Mascota:
    # declaramos el metodo __init__
    def __init__(self, nom):
        self.nombre=nom

	# creamos la primera funcion
	# para inicializar el atributo nombre
    def inicializar(self, nom):
        self.nombre = nom

	# creamos el segundo método
	# para mostrar el nombre
    def mostrar(self):
        print("Nombre: " , self.nombre)

# Crear objeto
Mascota1 = Mascota("Mira")
Mascota2= Mascota("Gordo")
# Usar métodos
Mascota1.mostrar()
Mascota2.mostrar()