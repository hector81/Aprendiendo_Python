'''
Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras 
el número no sea correcto , es decir no se encuentre en la lista, se repita el proceso.

La lista de número posibles [1, 3, 9]
'''
booleano = False
while booleano == False: # mientras el número no este en la lista, la condición será false
    numero = int(input('Introduce un número entero del 0 al 9: '))
    if numero > -1 and numero < 10:
        print(f"El número es {numero}")
        # recorremos y si está en la lista paramos el proceso
        for i in [1, 3, 9]:
            if numero == i:
                print(f"Estaba en la lista y se acaba el proceso")
                booleano = True  #cambiamos condicion    
    else: # en caso de que el número no sea del 0 al 9
        print("Has introducido un número que no es del 0 al 9.")