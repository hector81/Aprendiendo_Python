# max(), recibe más de un argumento, devuelve el mayor de ellos.
print("max(23, 12, 145, 88) ==> " , max(23, 12, 145, 88))
print("type(max(23, 12, 145, 88)) ==> " , type(max(23, 12, 145, 88)))

# min() tiene un comportamiento similar a max(), pero devuelve el mínimo.
print("min(23, 12, 145, 88) ==> " , min(23, 12, 145, 88))
print("type(min(23, 12, 145, 88)) ==> " , type(min(23, 12, 145, 88)))

# Con String da error
print('min(23, "12", 145, 88) ==> ' , min(23, "12", 145, 88))
print('type(min(23, "12", 145, 88)) ==> ' , type(min(23, "12", 145, 88)))