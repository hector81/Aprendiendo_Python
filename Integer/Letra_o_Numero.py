# Escriba un programa que determine si un caracter ingresado es letra, número, o
# ninguno de los dos. En caso que sea letra, determine si es mayúscula o
# minúscula.
def introducirCaracter():
     while True:
         try:
             caracter = input("Por favor ingrese un solo caracter: ")
             if len(caracter) == 1:
                 print("El caracter es " + caracter)
                 return caracter
                 break
             else:
                print("Solo un caracter por favor")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


caracter = introducirCaracter()

if caracter.isdigit():
    print("El caracter es un número")
elif caracter.isupper():
   print("El caracter es una letra mayuscula")
elif caracter.islower():
   print("El caracter es una letra minuscula")
else:
    print("El caracter no es letra ni número")
