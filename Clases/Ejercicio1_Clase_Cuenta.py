# 1. Cree una clase llamada Cuenta. Como atributo tendrá un número float llamado saldo,
# con una cantidad inicial de 0 euros. Tendrá dos métodos: ingresar, con un parámetro
# que indica la cantidad a sumar al saldo. retirar, con un parámetro que será un
#  número float de euros a restar del saldo. Cree un programa para
#   ingresar 125.23, 503.4 y 50 euros y luego retire, 333.34 euros.
#    Muestre tras cada operación, el saldo de la cuenta


# clase
class Cuenta:
    # atributo
    saldo = 0.0

    # constructor
    def __init__(self, saldo):
        self.__saldo = saldo

    # metodos
    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def ingresar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        self.__saldo -= cantidad

miCuenta = Cuenta(0.0)
ingreso1 = 125.23
ingreso2 = 503.4
ingreso3 = 50.0
retiro1 = 333.34

print("Mi saldo actual es " + str(miCuenta.getSaldo()))
print("Hago un primer ingreso de " + str(ingreso1) + " euros en mi cuenta")
miCuenta.ingresar(ingreso1)
print("Despues de mi primer ingreso mi saldo es " + str(miCuenta.getSaldo()))

print("Hago un segundo ingreso de " + str(ingreso2) + " euros en mi cuenta")
miCuenta.ingresar(ingreso2)
print("Despues de mi segundo ingreso mi saldo es " + str(miCuenta.getSaldo()))

print("Hago un tercer ingreso de " + str(ingreso3) + " euros en mi cuenta")
miCuenta.ingresar(ingreso3)
print("Despues de mi tercer ingreso mi saldo es " + str(miCuenta.getSaldo()))

print("Ahora hago un retiro de " + str(retiro1) + " euros de mi cuenta")
miCuenta.retirar(retiro1)
print("Despues de este retiro mi saldo es " + str(miCuenta.getSaldo()))
