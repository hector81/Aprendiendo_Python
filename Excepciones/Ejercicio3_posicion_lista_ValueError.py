'''
EJERCICIOS EXCEPCIONES
3. Función que recibe una lista y el elemento a buscar, devolviendo
  su posición si existe, y -1 en caso de que no (ValueError)
  [Pista: podemos usar la función list.index(value)]
'''


def encontrarPosicion_Elemento_enLista(lista,elemento):
    while True:
        try:
            return lista.index(elemento)
            break
        except ValueError:
            return -1


listaAnimales = ["Perro", "Gato", "Murcielago", "Cobra", "Avispa"]
print(listaAnimales)
animal1 = "Cobra"
print(f"El elemento 1 a buscar es {animal1}")
print(f"El elemento está en la posición = {encontrarPosicion_Elemento_enLista(listaAnimales,animal1)}")


animal2 = "Orca"
print(f"El elemento 2 a buscar es {animal2}")
print(f"El elemento está en la posición = {encontrarPosicion_Elemento_enLista(listaAnimales,animal2)}")
