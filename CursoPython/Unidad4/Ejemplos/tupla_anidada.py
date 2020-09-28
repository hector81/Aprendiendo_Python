x = (123,'Algebra',[50,70],5,73.25)
print(x)

print(x[2]) # devuelve lista situada en tercer elemento

print(x[2][1])# Se requiere un segundo índice para llegar al contenido del componente de tipo lista
# devuelve segundo elemento de la lista situada en tercer elemento

x[2][1] = 75 # Se pueden modificar elementos de la lista
print(x[2][1])

print(x)
