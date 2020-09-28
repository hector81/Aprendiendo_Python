'''
Cada función genera su propio espacio de nombres cada vez que es invocada. Cada uno de estos espacios
 de nombres es un ámbito local.

La función locals() devuelve el contenido de nombres del ámbito local como un objeto de tipo dict.

Cuando se invoca la función dir() sin argumentos desde dentro de una función, ésta devuelve un objeto
 de tipo lista con el listado de nombres del ámbito local.
'''
ab = "ab"
def ambitos():
    lista = [1, 2, 3]
    nulo = None
    print('Espacio de nombres en el ámbito local:')
    print(locals(), dir())
    print('Espacio de nombres en el ámbito global:')
    print(globals())

ambitos()