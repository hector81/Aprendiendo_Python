texto = "Una cadena"
# a
print("texto[5] == >" , texto[5]) # a
# El último carácter es -1, el penúltimo -2, etc.
print("texto[-1] == >" , texto[-1]) # a
print("texto[-2] == >" , texto[-2]) # n

#Esto imprime una sección de la cadena, comenzando en el indice 3, y terminando en el 6
print("texto[3:7] == >" , texto[3:7]) # ' cad'
print("texto[3:] == >" , texto[3:]) # 'cadena'
print("texto[:3] == >" , texto[:3]) # 'Una'

#Además, puedes utilizar un tercer indice para indicar los saltos en el rango acotado.
print("texto[::2] == >" , texto[::2]) # esto devuelve los caracteres situados en las posiciones pares
# 'uacdn'
print("texto[1::2] == >" , texto[1::2]) # esto devuelve los caracteres situados en las posiciones impares
# 'n aea'
