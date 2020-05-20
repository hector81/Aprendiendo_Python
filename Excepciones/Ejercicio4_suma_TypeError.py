'''
EJERCICIOS EXCEPCIONES
4. Función que recibe una lista y calcula la suma de todos los elementos, devolviendo
 None en caso de que alguno de los elementos no pueda sumarse (TypeError)
  [Pista: ¡la función sum() está a nuestra disposición!]
'''
def suma_Elementos_Lista(lista):
    while True:
        try:
            return sum(lista)
            break
        except TypeError:
            return None

lista1 = [1,55,8,22,56]
print(f"Lista 1 = {lista1}")
print(f"El resultado de la suma de los elementos de la lista 1 es = {suma_Elementos_Lista(lista1)}")

lista2 = [1,1,1,55,8.25,22.369,56]
print(f"Lista 2 = {lista2}")
print(f"El resultado de la suma de los elementos de la lista 1 es = {suma_Elementos_Lista(lista2)}")

lista3 = [1,1,1,55,"5555",22.369,56]
print(f"Lista 2 = {lista3}")
print(f"El resultado de la suma de los elementos de la lista 1 es = {suma_Elementos_Lista(lista3)}")
