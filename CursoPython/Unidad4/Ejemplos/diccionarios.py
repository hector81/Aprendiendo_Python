# clave: valor
diccionario = {'nombre':'Juan', 'apellido':'Garcia', 'edad':'21', 'curso':['python', 'Django']}

#acccede a diccionario mediante sus claves
print(diccionario['nombre']) # Juan
print(diccionario['apellido']) # Garcia
print(diccionario['edad']) # 21
print(diccionario['curso']) # ['python', 'Django']

#acccede a elemento de la lista del diccionario mediante sus clave
print(diccionario['curso'][1]) # Django


# Definición de un diccionario nulo.
dic={}
print(dic)