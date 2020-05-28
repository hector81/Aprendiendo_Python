def introducirPalabra():
     while True:
         try:
             palabra = input("Por favor ingrese una palabra: ")
             if palabra != '':
                 print("La palabra es " + palabra)
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


introducirPalabra()
