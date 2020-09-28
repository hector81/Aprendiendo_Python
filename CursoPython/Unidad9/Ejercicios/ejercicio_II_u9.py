# creamos la clase Cuenta
''' CLASE PADRE CUENTA '''
class Cuenta:
    """clase Cuenta
    """
    # declaramos el metodo __init__
    def __init__(self):
        self.titular=input("Ingrese el nombre de titular: ")
        self.cantidad=float(input("Ingrese la cantidad inicial de su cuenta: "))

    # Metodo para mostrar los datos de la cuenta
    def mostrar(self):
        """Metodo para mostrar los datos de la clase cuenta."""
        print(f"El nombre del titular de la cuenta es {self.titular} y su saldo inicial es de {self.cantidad} euros.")

''' SUBCLASE CUENTAHORRO QUE HEREDA DE LA CLASE PADRE CUENTA '''
# creamos la subclase CuentaAhorro que hereda de Cuenta
class CuentaAhorro(Cuenta):
    """subclase CuentaAhorro que hereda de Cuenta
    """
    # declaramos el metodo __init__ que sirve como método para heredar los datos
    def __init__(self):
        super().__init__() # llamamos al constructor de la clase Cuenta

    # metodo para mostrar la información heredada.
    def mostrar(self):
        """Metodo para mostrar los datos de la subclase CuentaAhorro y la clase padre cuenta."""
        super().mostrar() # llamamos al metodo mostrar de la clase que hereda, Cuenta

''' SUBCLASE PLAZOFIJO QUE HEREDA DE LA CLASE PADRE CUENTA '''
# creamos la subclase PlazoFijo que hereda de Cuenta
class PlazoFijo(Cuenta):
    """subclase PlazoFijo que hereda de Cuenta
    """
    # declaramos el metodo __init__ que sirve como método para heredar los datos
    def __init__(self):
        super().__init__() # llamamos al constructor de la clase Cuenta
        self.plazo=int(input("Introduce un plazo en años: ")) # atributo propio de la subclase
        self.interes=float(input("Introduce el interés del plazo fijo en un %: ")) # atributo propio de la subclase

    # Metodo para obtener el importe del interés
    def obtener_importe_interes(self):
        """Metodo para obtener el importe del interés mediante la formula (cantidad*interés/100)*plazo."""
        importe_interes = (self.cantidad * self.interes/100) * self.plazo
        return importe_interes

    def mostrar(self):
        """Metodo para mostrar la información, datos del titular, plazo, interés y total de interés."""
        super().mostrar() # llamamos al metodo mostrar de la clase que hereda, Cuenta
        print(f"El plazo del plazo fijo es {self.plazo} años, el interés anual es el {self.interes}% y el total de interés es {self.obtener_importe_interes()}")

# Ahora probamos las clases

# instanciamos la subclase CuentaAhorro creando un objeto
cuentaAhorro1 = CuentaAhorro()
# probamos su metodo
cuentaAhorro1.mostrar()

# instanciamos la subclase PlazoFijo creando un objeto
plazoFijo1 = PlazoFijo()
# probamos su metodo
plazoFijo1.mostrar()

