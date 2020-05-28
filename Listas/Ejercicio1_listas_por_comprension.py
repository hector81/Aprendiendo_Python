# FUNCIONES
def leerListaNumeros(x):
    stringNumeros = ""
    for numero in x:
        stringNumeros += str(numero) + " , "
    print(f"Lista números = " + stringNumeros[0:len(stringNumeros)-3])

def leerListaPersonas(personas):
    stringPersonas = ""
    for persona in personas:
        stringPersonas += persona + " , "
    print(f"Lista personas = " + stringPersonas[0:len(stringPersonas)-3])

def extraerNúmerosImpares(x):
    stringNumeros = ""
    for numero in x:
        if numero%2 != 0:
            stringNumeros += str(numero) + " , "
    print(f"Lista números impares = " + stringNumeros[0:len(stringNumeros)-3])

def filtrarNumerosMenorCinco(x):
    if x > 5:
        return False
    else:
        return True

def devolverListaMapaLambdaCaudrado(lista):
    return list(map(lambda x: x ** 2, lista))

# VARIABLES
listaNumeros = [8, 2, 3 , -1, 2, -5, 7]
personas = ["Sara","Pedro","Miguel"]

# OPERACIONES
leerListaNumeros(listaNumeros)
leerListaPersonas(personas)
extraerNúmerosImpares(listaNumeros)

numeros = filter(filtrarNumerosMenorCinco, listaNumeros)
listaString = ""
for num in numeros:
    listaString += str(num) + " , "
print(f"Lista números menores que 5 = " + listaString[0:len(listaString)-3])

print(f"Lista números Lsita Mapa Lambda al cuadrado = {devolverListaMapaLambdaCaudrado(listaNumeros)}")
