def introducirPalabra():
     while True:
         try:
             palabra = input("Por favor ingrese una palabra: ")
             if palabra != '':
                 print("La palabra es " + palabra)
                 return palabra
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


palabra = introducirPalabra()

def numeroLetrasPalabra(palabra):
    palabra = palabra.strip() # quitamos espacios blanco
    longitud = len(palabra)
    print('La palabra tiene este numero de letras = ' + str(longitud) )


numeroLetrasPalabra(palabra)
