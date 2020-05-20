# 6. Modifique la clase Cuenta del ejercicio 1. Haga que el atributo saldo
#  quede oculto. Cuando alguien desee leer ese atributo, debe escribir un
# número pin. Ese valor se introducirá como parámetro de la función
# leer_saldo, que agregará como nuevo método de la clase. El PIN para poder
# realizar la operación será 3210. Ahora que la variable saldo está oculta,
# ¿podría acceder a ella para mostrar su contenido sin conocer el PIN?.
# En caso afirmativo, explique cómo

# clase
class Cuenta2:
    # atributo

    # constructor
    def __init__(self,saldo = 0.0,numeroPin = 3210):
        self.__saldo = saldo  # atributo oculto
        self.__numeroPin = numeroPin  # atributo oculto

    # metodos
    def __getSaldo(self):
        return self.__saldo

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def getNumeroPin(self):
        return self.__numeroPin

    def setNumeroPin(self, numeroPin):
        self.__numeroPin = numeroPin

    def ingresar(self, cantidad):
        self.__saldo += cantidad
        print(f'Has ingresado {self.__saldo} euros de tu cuenta')

    def retirar(self, cantidad):
        self.__saldo -= cantidad
        print(f'Has retirado {self.__saldo} euros de tu cuenta')

    def leer_saldo (self, numeroPin):
        if numeroPin == self.__numeroPin:
            print(f'PIN correcto. Tu saldo es de {self.__saldo}')
        else:
            print(f'PIN incorrecto. No puedes acceder al saldo')

    def comprobarNumeroPin(self, numeroPin):
        boolComp = False
        if self.__numeroPin == numeroPin:
            boolComp = True
        return boolComp

    def comprobarHaySaldo_paraRetiro(self, cantidad):
        boolComp = False
        if self.__saldo < cantidad:
            boolComp = True
        return boolComp


# metodos
def introducirNumero():
     while True:
         try:
             numero = int(input(f'Por favor ingrese un número: '))
             if numero > 0:
                 return numero
                 break
             else:
                 print(f'Debe ser una cantidad positiva')
         except ValueError:
             print(f'No era válido. Intente nuevamente...')

def introducirCantidad():
     while True:
         try:
             cantidad = float(input(f'Por favor ingrese una cantidad: '))
             if cantidad > 0.0:
                 return cantidad
                 break
             else:
                 print(f'Debe ser una cantidad positiva')
         except ValueError:
             print(f'No era válido. Intente nuevamente...')

def mostrarOpciones():
     print(f'1-Hacer un ingreso')
     print(f'2-Retirar una cantidad')
     print(f'3-Ver tu saldo')
     print(f'4-Salir')

# variables
miCuenta2 = Cuenta2()
salir = False
numeroPin = 0
# OPERACIONES
while salir == False:
    mostrarOpciones()
    opcion = introducirNumero()
    if opcion == 1:
        print(f'Pon tu número PIN')
        numeroPin = introducirNumero()
        if miCuenta2.comprobarNumeroPin(numeroPin) == True:
            cantidad = introducirCantidad()
            miCuenta2.ingresar(cantidad)
        else:
            print(f'El número PIN no es correcto. Intente de nuevo')
    elif opcion == 2:
        print(f'Pon tu número PIN')
        numeroPin = introducirNumero()
        if miCuenta2.comprobarNumeroPin(numeroPin) == True:
            if miCuenta2.comprobarHaySaldo_paraRetiro(cantidad) == False:
                cantidad = introducirCantidad()
                miCuenta2.retirar(cantidad)
            else:
                print(f'No hay saldo suficiente en tu cuenta')
        else:
            print(f'El número PIN no es correcto. Intente de nuevo')
    elif opcion == 3:
        print(f'Pon tu número PIN')
        numeroPin = introducirNumero()
        if miCuenta2.comprobarNumeroPin(numeroPin) == True:
            miCuenta2.leer_saldo(numeroPin)
        else:
            print(f'El número PIN no es correcto. Intente de nuevo')
    elif opcion == 4:
        salir = True
