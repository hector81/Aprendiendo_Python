'''
Realice un programa que pida un número mayor que 1 por pantalla y calcule su tabla de multiplicar
Después que muestre el resultado por pantalla.
'''
booleano = False
while booleano == False: # mientras el número sea menor que 2 volvera a preguntarte el número
    numero = int(input('Introduce un número mayor que 1: '))
    if numero > 1:
        for i in range(1,11):# recorremos del 1 al 10, multiplicamos e imprimimos
            multiplicacion = numero * i
            print(f"{numero} X {i} = {multiplicacion}")
            booleano = True
    else: # en caso de que el número sea menor que 2
        print("Has introducido un número que es menor que 2.")
