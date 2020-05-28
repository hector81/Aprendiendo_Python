def introducirFrase():
     while True:
         try:
             frase = input("Por favor ingrese una frase: ")
             if frase != '':
                 return frase
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")
# fin funcion ########################################################

def introducirPalabra():
     while True:
         try:
             frase = input("Por favor ingrese una palabra: ")
             if frase != '':
                 return frase
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")
# fin funcion ########################################################

def numeroRepeticionesPalabra_EnFrase(palabra,frase):
    numRep = 0
    # recorremos la frase y separamos palabra
    for palabraX in frase.split():
        #sumamos repeticiones
        if palabraX == palabra:
            numRep = numRep + 1
    return numRep
# fin funcion ########################################################

def comprobarRepeticionesArray(elemento,arrayEnviado):
    boolComp = False
    for i in range(len(arrayEnviado)):
        if str(elemento) == str(arrayEnviado[i]):
            boolComp = True

    return boolComp
# fin funcion ########################################################


def devolverTamanio_elementos_lista(elemento):
    return len(elemento)
# fin funcion ########################################################

def numeroRepeticionesPalabra_EnFrase(palabra,frase):
    numRep = 0
    # recorremos la frase y separamos palabra
    for palabraX in frase.split():
        #sumamos repeticiones
        if palabraX == palabra:
            numRep = numRep + 1
    return numRep
# fin funcion ########################################################

def operaciones(frase):
    arraySinRep = []
    # creamos un array sin repeticiones
    for palabraX in frase.split():
        if comprobarRepeticionesArray(palabraX,arraySinRep) == False:
            arraySinRep.append(palabraX)

    # creamos una tupla con una lista vaca
    fraseTupla = ()
    lista=list(fraseTupla)

    # y la rellenamos con el arraySinRep
    for i in range(len(arraySinRep)):
        lista.append(arraySinRep[i])
    #ya tenemos la tupla sin repeticiones
    fraseTupla = tuple(lista)
    # ordenamos las palabras por alfabeto
    sorted(fraseTupla)
    # con map sabremos cuanto mide cada elemento
    x = map(devolverTamanio_elementos_lista, fraseTupla)
    arrayTamanio = list(x)

    # y recorremos
    for i in range(len(fraseTupla)):
        print(fraseTupla[i] + ' aparece ' + str(numeroRepeticionesPalabra_EnFrase(fraseTupla[i],frase)) + ' veces en la frase y tiene ' + str(arrayTamanio[i]) + ' letras')
# fin funcion ########################################################


frase = introducirFrase()
operaciones(frase)
