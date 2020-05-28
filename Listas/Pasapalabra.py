# funciones
def comprobarLetraAbecedario(letra):
    boolBomp = False
    arrayAbecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
    for i in range(len(arrayAbecedario)):
        if letra.upper() == arrayAbecedario[i].upper():
            boolBomp = True
    return boolBomp
###############################################################################
def introducirLetra():
     while True:
         try:
             letra = input("Por favor ingrese una letra: ")
             if len(letra) == 1:
                 if comprobarLetraAbecedario(letra) == True:
                    print("La letra es " + letra.upper())
                    return letra.upper()
                    break
                 else:
                    print("Debe ser solo una letra del abecedario")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")
###############################################################################
def comprobarLetrasRepetidasIntentos(letra,arrayIntentosLetras):
    boolBomp = False
    for i in range(len(arrayIntentosLetras)):
        if letra.upper() == arrayIntentosLetras[i].upper():
            boolBomp = True
    return boolBomp
###############################################################################
def comprobarLetraEsteEnFrase(FraseAleatoria,letra):
    boolBomp = False
    for i in range(len(FraseAleatoria)):
        if letra.upper() == FraseAleatoria[i].upper():
            boolBomp = True
    return boolBomp
###############################################################################
def comprobarPosicionCoincide(arrayComp,numero):
    boolBomp = False
    for i in range(len(arrayComp)):
        if numero == arrayComp[i]:
            boolBomp = True
    return boolBomp
###############################################################################
def comprobarPalabraCompleta(palabraVacia):
    boolComp = False
    for i in range(len(palabraVacia)):
        if palabraVacia[i] == '-':
            boolComp = True
    return boolComp

def sustituirPosicionFrase(FraseVacia,num,letra):
    arrayPalabra = list(FraseVacia.split(" ")) # convertimos string a array
    nu = int(num)
    arrayPalabra[nu] = str(letra)
    # convertimos  array a string
    palabraNueva = ''

    for i in range(len(arrayPalabra)):
        if arrayPalabra[i] == ' ':
            palabraNueva = palabraNueva + ''
        else:
            palabraNueva = palabraNueva + arrayPalabra[i] + ' '

    return palabraNueva


###############################################################################
def ponerLetraEnFraseVacia(FraseVacia,FraseAleatoria,letra):
    #averiguamos posicion o posiciones
    posicion = []
    num = 0
    for i in range(len(FraseAleatoria)):
        if letra.upper() == FraseAleatoria[i].upper():
            posicion.append(i)

    #sustituimos posicion por letra
    for i in range(len(FraseAleatoria)):
        if comprobarPosicionCoincide(posicion,i) == True:
            num = int(i)
            FraseVacia = sustituirPosicionFrase(FraseVacia,num,letra)

    return FraseVacia
###############################################################################
# variables
FraseAleatoria = 'Los huevos fritos se pueden poner con chorizo o patatas'
FraseAleatoria = FraseAleatoria.upper()

FraseVacia = ''
for i in range(len(FraseAleatoria)):
    if FraseAleatoria[i] == ' ':
        FraseVacia = FraseVacia + ' '
    else:
        FraseVacia = FraseVacia + '- '

numeroIntentos = 8
arrayIntentosLetras = []
###############################################################################


# operaciones
print('Juega al ahorcado. Adivina la palabra en ingles. Puedes poner 8 letras como máximo')
print(FraseAleatoria)
print(FraseVacia)
while numeroIntentos != 0:
    letra = introducirLetra()
    if comprobarLetrasRepetidasIntentos(letra,arrayIntentosLetras) == True:
        print('La letra está repetida, Ya las puesto antes')
    else:
        arrayIntentosLetras.append(letra)
        if comprobarLetraEsteEnFrase(FraseAleatoria,letra) == True:
            print('La letra está en la palabra')
            FraseVacia = ponerLetraEnFraseVacia(FraseVacia,FraseAleatoria,letra)
            print(FraseVacia)
            if comprobarPalabraCompleta(FraseVacia) == False:
                print('Enhorabuena. Has acertado')
                numeroIntentos = 0
        else:
            print('La letra no está en la palabra')
            numeroIntentos = numeroIntentos -1
            print('Te quedan ' + str(numeroIntentos) + ' intentos')

if numeroIntentos == 0:
    print('La palabra era ' + FraseAleatoria)
