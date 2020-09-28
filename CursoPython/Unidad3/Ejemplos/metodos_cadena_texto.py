# Asignar un texto a una variable te tipo str.
texto = "una cadena"
print(texto)
#Devuelve un entero(int) con la longitud en caracteres del texto, incluidos puntuación y espacios.
len(texto)
# 10
print(len(texto))

#Ubicación de la primera letra que cumple, en este caso la letra "a".
texto.index("a")
# 2
print(texto.index("a"))

#Cuenta el número de veces que aparece la letra buscada, en este caso 3.
texto.count("a")
# 3
print(texto.count("a"))

#Convierte la cadena de texto en mayúsculas.
texto.upper()
# 'UNA CADENA'
print(texto.upper())

#Convierte la cadena de texto en minúsculas.
texto.lower()
# 'una cadena'
print(texto.lower())

#Devuelve true o false dependiendo de si la cadena empieza como has especificado.
texto.startswith("Hola")
# False
print(texto.startswith("Hola"))
# True
print(texto.startswith("una"))

# Devuelve true o false dependiendo de si la cadena termina como has especificado
texto.endswith("asdfasdfasdf")
# False
print(texto.endswith("asdfasdfasdf"))
# True
print(texto.startswith("cadena"))