def retorno_multiple():
    return "Cadena de texto", 47, [1,2,3]
#devulve una tupla con los datos
print("Tupla = " , retorno_multiple())
tupla = retorno_multiple()
print("1º Elemento del retorno = " , tupla[0])
print("2º Elemento del retorno = " , tupla[1])
print("3º Elemento del retorno = " , tupla[2])

# transformamos elementos  reasignados a una variable en particular.
cadena, numero, lista = retorno_multiple()
print(cadena, type(cadena))
# Cadena de texto <type 'str'>
print(numero, type(numero))
# 47 <type 'int'>
print(lista, type(lista))
# [1, 2, 3] <type 'list'>