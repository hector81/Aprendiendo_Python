import random
# FUNCIONES
########################################################
# funcion para comprobar repetidos en array
def comprobarRepetidosArrayNumero(arrayComp , numero):
    comp = False
    for elemento in arrayComp:
        if elemento == numero:
            comp = True
    return comp


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

# creo mil primitivas
for i in range(0, 1000):
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
    print('PRIMITIVA ' + str(i+1))
    for j in range(len(primitiva)):
        print(primitiva[j], end=' ')
    print()
    primitiva.clear()
