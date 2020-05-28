'''
4. Función que recibe una lista de enteros y calcula su media aritmética.
'''
def devolverMediaAritmeticaListaEnteros(listaEnteros):
    sumaTotal = 0
    for numero in listaEnteros:
        sumaTotal += numero
    return sumaTotal/len(listaEnteros)


listaEnteros = [22,5,6,88,17,59,90]
print(f'Media aritmetica = {devolverMediaAritmeticaListaEnteros(listaEnteros)}')
