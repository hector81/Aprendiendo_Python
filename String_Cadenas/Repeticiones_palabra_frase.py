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

frase = introducirFrase()
palabra = introducirPalabra()
print('La palabra ' + palabra + ' se repite ' + str(numeroRepeticionesPalabra_EnFrase(palabra,frase)) + ' veces')
