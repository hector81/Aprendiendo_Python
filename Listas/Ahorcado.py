import urllib.request
import random
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
def comprobarLetraEsteEnPalabra(palabraAleatoria,letra):
    boolBomp = False
    for i in range(len(palabraAleatoria)):
        if letra.upper() == palabraAleatoria[i].upper():
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

def sustituirPosicionPalabra(palabra,numero,letra):
    arrayPalabra = list(palabra.split(" ")) # convertimos string a array
    nu = int(numero)
    arrayPalabra[nu] = str(letra)

    # convertimos  array a string
    palabraVacia = ''
    for i in range(len(arrayPalabra)):
        palabraVacia = palabraVacia + arrayPalabra[i]

    palabraNueva = ''
    for i in range(len(palabraVacia)):
        palabraNueva = palabraNueva + palabraVacia[i] + ' '

    return palabraNueva

###############################################################################
def ponerLetraEnPalabraVacia(palabraVacia,palabraAleatoria,letra):
    #averiguamos posicion o posiciones
    posicion = []
    num = 0
    for i in range(len(palabraAleatoria)):
        if letra.upper() == palabraAleatoria[i].upper():
            posicion.append(i)
    #sustituimos posicion por letra
    for i in range(len(palabraAleatoria)):
        if comprobarPosicionCoincide(posicion,i) == True:
            num = int(i)
            palabraVacia = sustituirPosicionPalabra(palabraVacia,num,letra)

    return palabraVacia
###############################################################################
# variables
Word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(Word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()
# print(words)
tamanioDiccionario = len(words) -1
numeroAleatorio = random.randint(0, tamanioDiccionario)

palabraAleatoria = words[numeroAleatorio]
palabraAleatoria = palabraAleatoria.upper()
tamanioPalabraAleatoria  = len(palabraAleatoria)

palabraVacia = ''
for i in range(len(palabraAleatoria)):
    palabraVacia = palabraVacia + '- '

numeroIntentos = 8
arrayIntentosLetras = []
###############################################################################


# operaciones
print('Juega al ahorcado. Adivina la palabra en ingles. Puedes poner 8 letras como máximo')
print(palabraVacia)
print(palabraAleatoria)
while numeroIntentos != 0:
    letra = introducirLetra()
    if comprobarLetrasRepetidasIntentos(letra,arrayIntentosLetras) == True:
        print('La letra está repetida, Ya las puesto antes')
    else:
        arrayIntentosLetras.append(letra)
        if comprobarLetraEsteEnPalabra(palabraAleatoria,letra) == True:
            print('La letra está en la palabra')
            palabraVacia = ponerLetraEnPalabraVacia(palabraVacia,palabraAleatoria,letra)
            print(palabraVacia)
            if comprobarPalabraCompleta(palabraVacia) == False:
                print('Enhorabuena. Has acertado')
                numeroIntentos = 0
        else:
            print('La letra no está en la palabra')
            numeroIntentos = numeroIntentos -1
            print('Te quedan ' + str(numeroIntentos) + ' intentos')

if numeroIntentos == 0:
    print('La palabra era ' + palabraAleatoria)
