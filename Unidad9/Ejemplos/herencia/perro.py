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

# creamos la clase perro que hereda de mascota
#Subclase perro que hereda de mascota
class Perro(Mascota):
    """Iria el Docstring
    """

    # declaramos el metodo __init__
    def __init__(self):
        super().__init__() # llamamos al constructor de la clase mascota
        self.peso=int(input("El peso del perro: "))
    # ESTA FUNCION YA ESTA EN MASCOTA
    def mostrar(self):
        super().mostrar() # llamamos al metodo mostrar de la clase que hereda, mascota
        print("Peso: " , self.peso)
 
    #A continuación, vas a crear el método "bozal" de clase "perro", y comprobarás si el perro debe llevar bozal, dependiendo de su peso:
    def bozal(self):
        if self.peso > 24:
            print("El perro es muy grande " , self.nombre , " debe llevar puesto bozal cuando salga a la calle.")
        else:
            print("El perro " , self.nombre , " no debe llevar puesto bozal cuando salga a la calle.")

# Asigna la clase a una variable.
Perro1 = Perro()
# Si quieres mostrar los datos del objeto "perro".
Perro1.mostrar()
# Si quieres comprobar si la mascota "perro" necesita bozal, haz lo siguiente:
Perro1.bozal()


