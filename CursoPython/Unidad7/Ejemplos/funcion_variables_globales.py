def nombre_global():
    global nombre # la creamos global porque nos interesa sea global y no local
    nombre = "Hola Juan"

#print(nombre) # si intentara llamar a la variable daria error porque no esta definida
# asi que primero llamo a la funcion y con esa crea la variable y ya podemos llamarla
nombre_global()
print(nombre)
