# La función pow() si recibe dos argumentos, eleva el primero argumento a la potencia del segundo.
print("pow(2, 3) ==>  " , pow(2, 3) ) # es igual que -> 2 ** 3 # da  8
print("pow(10, 2) ==> " , pow(10, 2)) # da 100
print("pow(10, -2) ==> " , pow(10, -2)) # da 13

# Si recibe un tercer argumento opcional, este funcionará como módulo.
print("pow(3, 4, 17) ==> " , pow(3, 4, 17)) # da lo mismo hacer esto # da 13
print("3 ** 4 % 17 ==> " , 3 ** 4 % 17) # que esto # da 13