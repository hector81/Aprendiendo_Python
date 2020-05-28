'''
1. Función que recibe una lista de enteros y devuelve la suma de todos sus elementos.
Sin utilizar sum(), claro está...
'''
def sumarListaEnteros(listaEnteros):
    sumaTotal = 0
    for numero in listaEnteros:
        sumaTotal += numero
    return sumaTotal

listaEnteros = [22,5,6,88,17,59,90]
print(f'Suma = {sumarListaEnteros(listaEnteros)}')
