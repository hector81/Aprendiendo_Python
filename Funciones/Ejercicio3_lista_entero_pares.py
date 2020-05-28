'''
3. Función que recibe una lista de enteros y devuelve otra lista con aquellos
  que son pares .
'''
def devolverListaEnteros(listaEnteros):
    listaPares = []
    for numero in listaEnteros:
        if numero%2 == 0:
            listaPares.append(numero)
    return listaPares

listaEnteros = [22,5,6,88,17,59,90]
print(f'Lista pares = {devolverListaEnteros(listaEnteros)}')
