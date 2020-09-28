''' Dict() '''
print("Dict()")
#Su parámetro(contenido del paréntesis) es una representación de un diccionario 
# y si se puede, devuelve un diccionario.
dic1 =  dict(nombre='Juan', apellido='García', edad=21, curso=['python','Django'])
print(dic1)

''' Zip() '''
print("Zip()")
#deben tener el mismo número de elementos. Se devolverá un diccionario relacionando 
# el elemento[i] de cada una de las listas, cadena o tupla. RELACIONA CLAVE VALOR
dic2 = dict(zip('aceg',[2,4,6,8]))
print(dic2)

''' Items() '''
print("Items()")
#Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será 
# la clave y el segundo, su valor.
dic3 =   {'a': 2, 'c': 4, 'e': 6, 'g': 8}
items = dic3.items()
print(items)

''' Keys() '''
print("Keys()")
#Devuelve una lista de elementos de las claves de nuestro diccionario.
dic4 =  {'a': 2, 'c': 4, 'e': 6, 'g': 8}
keys= dic4.keys()
print(keys)

''' Values() '''
print("Values()")
#Retorna una lista de elementos de los valores de nuestro diccionario.
dic5 =  {'a': 2, 'c': 4, 'e': 6, 'g': 8}
values= dic5.values()
print(values)

''' Clear() '''
print("Clear()")
#Elimina todos los elementos del diccionario, dejándolo vacío.
dic6 =  {'a': 2, 'c': 4, 'e': 6, 'g': 8}
dic6.clear()
print(dic6)

''' Copy() '''
print("Copy()")
#Retorna una copia del diccionario original.
dic = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
dic7 = dic.copy()
print(dic7)

''' Fromkeys() '''
print("Fromkeys()")
#Recibe como parámetros un iterable y un valor, devolviendo un diccionario que 
# contiene como claves los elementos del iterable con el mismo valor ingresado.
#  Si el valor no es ingresado, devolverá none para todas las claves.
dic8 = dict.fromkeys(['a','b','c','d'],1)
print(dic8)
dic8 = dict.fromkeys(['a','b','c','d'],)
print(dic8)

''' Get() '''
print("Get()")
#Parámetro es una clave y devuelve el valor de la clave. Si no lo encuentra, devuelve un objeto none.
dic9 = {'a': 2, 'c': 4, 'e': 6, 'g': 8, 'i':''}
valor = dic9.get('c')
print(valor)
valor = dic9.get('i')
print(valor)

''' Pop() '''
print("Pop()")
#Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.
dic10 = {'a': 2, 'c': 4, 'e': 6, 'g': 8}
print(dic10)
valor = dic10.pop('c')
print(valor)
print(dic10)

''' Setdefault() '''
print("Setdefault()")
#Funciona de dos formas. En la primera devuelve el valor dependiente de la clave introducida.
dic11 = {'a': 2, 'c': 4, 'e': 6, 'g': 8}
valor1 = dic11.setdefault('a')
print(valor1)
print(dic11)

#En la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.
dic12 = {'a': 2, 'c': 4, 'e': 6, 'g': 8}
valor2 = dic12.setdefault('i',10)
print(valor2)
print(dic12)

''' Uppadate() '''
print("Uppadate()")
#Recibe como parámetro otro diccionario. Si se tienen claves iguales, actualiza 
# el valor de la clave repetida; si no hay claves iguales, este par clave-valor es
#  agregado al diccionario.
dic13 = {'a': 2, 'c': 4, 'e': 6, 'g': 8}
dic14 = {'a':1, 'b':3, 'd':5, 'f':7 , 'h':10}
dic13.update(dic14)
print(dic13)
