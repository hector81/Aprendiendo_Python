'''
EJERCICIOS EXCEPCIONES
 5. Función que recibe una lista y un índice, y devuelve el elemento que
  ocupa dicha posición o None si el índice está fuera de los límites de
  la lista (¿Excepción?
'''
def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def devolverElemento_indice_lista(lista, indice):
    while True:
        try:
            return lista[indice]
            break
        except IndexError:
            return None

listaNombres = ["Carlos", "Roberto", "Fernando", "Jose María", "Ruben"]


print(listaNombres)
print(f"Elige un número de la lista")
numero = introducirNumero()
print(f"El elemento o nombre que ocupa dicha posicion en la lista es = {devolverElemento_indice_lista(listaNombres, numero)}")
