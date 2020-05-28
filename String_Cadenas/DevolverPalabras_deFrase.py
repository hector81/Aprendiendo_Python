def introducirFrase():
     while True:
         try:
             frase = input("Por favor ingrese una palabra: ")
             if frase != '':
                 print("La frase es " + frase)
                 return frase
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


frase = introducirFrase()

def devolverPalabras_Frase(frase):
    for palabra in frase.split():
        print(palabra)

devolverPalabras_Frase(frase)
