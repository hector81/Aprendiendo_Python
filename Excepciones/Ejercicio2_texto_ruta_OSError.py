'''
EJERCICIOS EXCEPCIONES
2. Programa que itere sobre una lista de cadenas de texto que contienen nombres
 de fichero hasta encontrar el primero que existe (OSError) [Pista: crear nuestra
  propia función, existe_fichero(ruta), que devuelve True o False]
'''

# buscar fichero = Ejercicio2_texto_ruta_OSError.py
def introducirNombreFichero():
     while True:
         try:
             fichero = input(f"Por favor ingrese un nombre de fichero: ")
             if fichero != '':
                 print(f"El fichero buscado es " + fichero)
                 return fichero
                 break
         except ValueError:
             print(f"Oops! No era válido. Intente nuevamente...")


def existe_fichero(fichero):
    while True:
        try:
            with open(fichero,"r") as ficheroBuscar:
                print(f"Fichero encontrado")
                break
        except OSError:
        	print(f"Fichero ' {fichero} ' no existe")
        finally:
            print(f"Operación terminada")
        break


fichero = introducirNombreFichero()
existe_fichero(fichero)
