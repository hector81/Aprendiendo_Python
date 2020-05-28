print("Calculadora básica ")
def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


print("Introduce el primer operador.")
numero1 = introducirNumero()

print("Introduce el segundo operador.")
numero2 = introducirNumero()

print("Elige el operador.")
operadores = ['+','-','*','/']
for i in range(len(operadores)):
    print('Operador' + str(i+1) + ' = ' + operadores[i])

print("Pon el número de operador.")
operador = 0
while operador < 1 or operador > 4:
    operador = introducirNumero()


eleccion = operador - 1
if eleccion == 0:
    print(str(numero1) + ' ' + str(operadores[eleccion]) + ' ' + str(numero2) + ' = ' + str(numero1+numero2))
elif eleccion == 1:
        print(str(numero1) + ' ' + str(operadores[eleccion]) + ' ' + str(numero2) + ' = ' + str(numero1-numero2))
elif eleccion == 2:
        print(str(numero1) + ' ' + str(operadores[eleccion]) + ' ' + str(numero2) + ' = ' + str(numero1*numero2))
elif eleccion == 3:
        print(str(numero1) + ' ' + str(operadores[eleccion]) + ' ' + str(numero2) + ' = ' + str(numero1/numero2))
