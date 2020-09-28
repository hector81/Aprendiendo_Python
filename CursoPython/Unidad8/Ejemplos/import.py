import calculadora
# Uso las funciones importadas
calculadora.suma(3,9)
calculadora.resta(3,9)
calculadora.multiplica(3,9)
calculadora.divide(3,9)

print('******************')
# igualo variables con las funciones importadas, y las uso como funciones directamente
suma = calculadora.suma
resta = calculadora.resta
multiplica = calculadora.multiplica
divide = calculadora.divide

suma(32,9)
resta(32,9)
multiplica(32,9)
divide(32,9)

