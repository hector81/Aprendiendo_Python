'''
Encuentra el factorial de un número usando un bucle while.
Un factorial de un número entero es ese número multiplicado por cada número entero entre sí y 1. 
Por ejemplo, 5 factorial (escrito "5!") es igual a  5 x 4  x 3 x 2 x 1 = 120.
Así que 6! = 720.
Ingresa por pantalla cualquier número y averigua cuál es su factorial.
Ejemplo: Si el número es 6, su código debe calcular e imprimir el producto, 720.
'''
booleano = False
multiplicacion_string = "" # para imprimir la multiplicación
factorial = 1 # inicamos a 1 para que la 1º multiplicacion no sea por 0
while booleano == False: # mientras que el número no sea menor que 1
    numero = int(input('Introduce un número mayor que 0: '))
    # comprobamos que el número no sea menor que 1
    if numero > 0:
        for i in range(numero, 0,-1): # recorremos el nº hacia atras hasta 1
            factorial = factorial * i # multiplicamos el factorial sucesivamente
            # esto es para el formato de la multiplicacion
            if i != 1:
                multiplicacion_string +=  f"{i} X "
            else:
                multiplicacion_string +=  f"{i}"
        print (f"{multiplicacion_string} = {factorial}") # factorial
        booleano = True # cambiamos la condición para salir del bucle
    else: # en caso de que el número sea menor que 1
        print("Has introducido un número que es menor que 1.")