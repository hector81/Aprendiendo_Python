import re
# https://www.w3schools.com/python/python_regex.asp
def introducirFrase():
     while True:
         try:
             palabra = input("Por favor ingrese una frase: ")
             if palabra != '':
                 return palabra
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def introducirPalabraPrimera():
     while True:
         try:
             palabra = input("Por favor ingrese la primera palabra a buscar: ")
             if palabra != '':
                 return palabra
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def introducirPalabraUltima():
     while True:
         try:
             palabra = input("Por favor ingrese la ultima palabra a buscar: ")
             if palabra != '':
                 return palabra
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


frase = introducirFrase()

palabraPrimera = introducirPalabraPrimera()
palabraUltima = introducirPalabraUltima()

busquedaBool = re.search("^" + str(palabraPrimera) + ".*" + str(palabraUltima) + "$", frase)

if (busquedaBool):
  print("La palabra primera y ultima están")
else:
  print("La palabra primera y ultima no están")
