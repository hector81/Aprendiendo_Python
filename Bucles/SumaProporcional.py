def doblar(veces,numero):
    arrayT = []
    arrayT.append(numero)
    while veces != 0:
        numero = numero * 2
        arrayT.append(numero)
        veces = veces - 1
    return arrayT

def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese el número que quieres multiplicar por el doble: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def introducirVeces():
     while True:
         try:
             x = int(input("Por favor ingrese el número de veces que quieres que se multiplique: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

numero = introducirNumero()
veces = introducirVeces()


arrayImprimir = doblar(veces,numero)

for i in range(len(arrayImprimir)):
    print('Numero multiplicado ' + str(i+1) + ' veces = ' + str(arrayImprimir[i]))
