# a y b son variables y func es una función
def operacion(a,b,func):
    return func(a,b)
 
def suma(x,y):
    return x + y
 
def resta(x,y):
    return x - y
 
def multiplica(x,y):
    return x * y
 
def divide(x,y):
    return x / y

#Hasta aquí has creado la funcion superior(operación) y las subfunciones
#(suma, resta, multiplica y divide) que se enviarán como parámetro a la función superior.
 
#Al llamar a la función podemos guardar el resultado en una variable.
 
resultado1 = operacion(6,5,suma)
print(resultado1)
 
resultado2 = operacion(14,5,resta)
print(resultado2)
 
#o bien directamente imprimir el resultado.
 
print(operacion(3,7,multiplica))

print(operacion(14,7,divide))