'''
Escribe un programa que pida dos números  por pantalla para crear un rango, a continuación, el 
 programa debe calcular la cantidad de números  pares y la cantidad de impares que hay en el rango 
 que has generado, desde el primero al último.
Recuerda que un número par siempre es divisible entre 2, es decir su resto es 0.
'''
booleano = False
pares = 0
impares = 0
while booleano == False: # mientras que los 2 números sean menores que 1 volvera a preguntarte los números
    numero1 = int(input('Introduce un 1º número mayor que 1: '))
    numero2 = int(input('Introduce un 2º número mayor que 1. Este tiene que ser mayor que el 1º número: '))
    # comprobamos que los dos números sean mayor que 1
    if numero1 > 0 and numero2 > 0:
        # comprobamos que el 2ºnumero sea mayor que el numero1, para que el rango no de error
        if numero2 > numero1: 
            for i in range(numero1,numero2+1):# recorremos del numero1 al numero2+1
                # sumamos pares e impares
                if i%2 == 0:
                    pares = pares + 1
                    print(f"{i} = Par.")
                else:
                    impares = impares + 1
                    print(f"{i} = impar.")
            print(f"Del número {numero1} al número {numero2} hay {pares} pares y {impares} impares")
            booleano = True
        else: 
            print("Recuerda que el número 1 debe ser menor que el 2.")
    else: # en caso de que alguno de los números sean menores que 1
        print("Has introducido un número que es menor que 2.")