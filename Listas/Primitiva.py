import random

########################################################
# FUNCIONES
########################################################
# funcion para comprobar repetidos en array
def comprobarRepetidosArrayNumero(arrayComp , numero):
    comp = False
    for elemento in arrayComp:
        if elemento == numero:
            comp = True
    return comp

# funcion para comprobar repetidos en array
def comprobarAciertosMiNumeroPorPrimitiva(arrayMisNumerosP, arrayPrimi):
    numAciertos = 0
    for i in range(len(arrayPrimi)):
        if comprobarRepetidosArrayNumero(arrayMisNumerosP , arrayPrimi[i]) == True:
            numAciertos = numAciertos + 1
    return numAciertos
########################################################

# introducir tus numeros de primitiva
print('Introduce tus numeros de la primitiva. Son 6 y no deben ser negativos, ni 0 ni mayor de 50')
contadorNumerosPrimitiva = 1
miPrimitiva = []
miNumero = 0
# ponemos numeros primitiva
while contadorNumerosPrimitiva < 7:
    # ponemos el numero
    miNumero = int(input('Escribe el numero ' + str(contadorNumerosPrimitiva) + ' = '))
    if miNumero < 1 or miNumero > 50:
        print('El número no es valido')
    else:
        if contadorNumerosPrimitiva == 1:
            miPrimitiva.append(miNumero)
            contadorNumerosPrimitiva = contadorNumerosPrimitiva + 1
            print('Numero introducido correctamente')
        else:
            # si es false el numero no esta repetido
            if comprobarRepetidosArrayNumero(miPrimitiva,miNumero) == False:
                miPrimitiva.append(miNumero)
                contadorNumerosPrimitiva = contadorNumerosPrimitiva + 1
                print('Numero introducido correctamente')
            else: # y si esta repetido
                print('El número está repetido')


# imprimir mis numeros
print("Tus numeros de quiniela son = " + str(miPrimitiva[0]) + " - " + str(miPrimitiva[1]) + " - " + str(miPrimitiva[2]) + " - " + str(miPrimitiva[3]) + " - " + str(miPrimitiva[4]) + " - " + str(miPrimitiva[5]) )


# creo las primitivas
arrayPrimitivas = []
primitiva = []
contPrimitivas = 1
numeroAleatorio = 0
aciertos0 = 0
aciertos1 = 0
aciertos2 = 0
aciertos3 = 0
aciertos4 = 0
aciertos5 = 0
aciertos6 = 0


print('Cuantas primitivas quieres crear para comparar tus numeros')
numPrim = int(input('Escribe el numero de pimitivas = '))

# creo mil primitivas
for i in range(0, numPrim):
    while contPrimitivas < 7:
        numeroAleatorio = random.randint(1, 50)
        # todo esto es para comprobar que cada primitiva no tiene numeros repetidos
        if contPrimitivas == 1:
            primitiva.append(numeroAleatorio)
            contPrimitivas = contPrimitivas + 1
        else:
            # si es false el numero no esta repetido
            if comprobarRepetidosArrayNumero(primitiva,numeroAleatorio) == False:
                primitiva.append(numeroAleatorio)
                contPrimitivas = contPrimitivas + 1

    contPrimitivas = 0

    #######################################
    print('PRIMITIVA ' + str(i+1))
    for j in range(len(primitiva)):
        print(primitiva[j], end=' ')
    print()

    #######################################
    # pongo primitiva en array arrayMultiple
    arrayPrimitivas.append(primitiva)
    # vacio array para la siguiente vuelta
    primitiva = []

# compruebo las primitivas
for i in range(len(arrayPrimitivas)):
    sorteoPrimitiva = arrayPrimitivas[i]
    numeroTotalAciertos = comprobarAciertosMiNumeroPorPrimitiva(miPrimitiva, sorteoPrimitiva)
    if numeroTotalAciertos == 0:
        aciertos0 = aciertos0 + 1
    elif numeroTotalAciertos == 1:
        aciertos1 = aciertos1 + 1
    elif numeroTotalAciertos == 2:
        aciertos2 = aciertos2 + 1
    elif numeroTotalAciertos == 3:
        aciertos3 = aciertos3 + 1
    elif numeroTotalAciertos == 4:
        aciertos4 = aciertos4 + 1
    elif numeroTotalAciertos == 5:
        aciertos5 = aciertos5 + 1
    elif numeroTotalAciertos == 6:
        aciertos6 = aciertos6 + 1


# imprimir mis numeros
print("Tus numeros de quiniela son = " + str(miPrimitiva[0]) + " - " + str(miPrimitiva[1]) + " - " + str(miPrimitiva[2]) + " - " + str(miPrimitiva[3]) + " - " + str(miPrimitiva[4]) + " - " + str(miPrimitiva[5]) )
print('TUS ACIERTOS ===>  ')
print('0 ACIERTOS   ' + str(aciertos0))
print('1 ACIERTOS   ' + str(aciertos1))
print('2 ACIERTOS   ' + str(aciertos2))
print('3 ACIERTOS   ' + str(aciertos3))
print('4 ACIERTOS   ' + str(aciertos4))
print('5 ACIERTOS   ' + str(aciertos5))
print('6 ACIERTOS   ' + str(aciertos6))
