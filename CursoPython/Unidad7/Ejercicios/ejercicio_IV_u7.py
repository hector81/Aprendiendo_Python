'''
Implementa un generador fibonacci que produce los diferentes números de la secuencia de Fibonacci, que 
tiene la forma:   0, 1, 1, 2, 3, 5, 8, 13, ...
Cuyos dos primeros valores son 0 y 1 por definición y el resto se calculan sumando los dos últimos 
valores de la sucesión.
'''
# esto es para introducir el número de números hasta el cual quieres que genere el fibonacci
booleano = False
while booleano == False:
    numero = int(input("Introduce hasta que número de números quieres generar la lista fibonacci = "))
    if numero < 1:# mientras sea un número menor que 1
        print("Tienes que poner un número mayor que 0.")
    else:
        booleano = True

def fibonacci(numero):
    """ funcion para crear lista fibonacci hasta cierto número de números como limite"""
    # variables locales inicializadas
    lista_fibonacci = [] # lista vacia
    contador = 0 # esto es para el contador de posiciones de la lista
    suma_2_anteriores = 0 # para la suma de las 2 posiciones anteriores
    while contador < numero: # mientras el contador no alcance N numero de veces
        if contador == 0 or contador == 1:# los dos primeros números serán siempre 0 y 1
            lista_fibonacci.append(contador) # añadimos a la lista
            yield lista_fibonacci[contador] # devolvemos lista por posicion
        else:
            suma_2_anteriores = lista_fibonacci[contador-1] + lista_fibonacci[contador-2] # sumamos 2 posiciones anteriores
            lista_fibonacci.append(suma_2_anteriores) # añadimos a la lista
            yield lista_fibonacci[contador]  # devolvemos lista
        contador = contador + 1 # aumentamos contador

#recorremos o iteramos la lista
for numero_fibo in fibonacci(numero):
    print(numero_fibo , end = ' ')
