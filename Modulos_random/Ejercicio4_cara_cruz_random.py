'''
EJERCICIOS
MÓDULO random
 4. Juguemos a cara o cruz. Dispone de 1000 euros. Cada apuesta es de 100 euros.
 Si gana duplica su apuesta. Si pierde, se queda sin 100 euros. Haga una simulación
  y comprueba en cuantas jugadas lo pierde todo
'''
import random
# FUNCIONES
def resultadoMoneda(numero):
    if numero == 1:
        return 'Cara'
    elif numero == 2:
        return 'Cruz'

# VARIABLES
resultadoPierdo = 0
resultadoGano = 0
cantidad = 1000
jugadas = 1

# OPERACIONES
while cantidad > 0: # and jugadas < 50:
    print(f"Jugada número {(jugadas )}")
    miMoneda = random.randint(1, 2)
    resultadoMonedaAleatoria = random.randint(1, 2)
    print(f"Mi apuesta es {resultadoMoneda(miMoneda)}. Resultado = {resultadoMoneda(resultadoMonedaAleatoria)}")
    if miMoneda == resultadoMonedaAleatoria:
        cantidad = cantidad + 200
        print(f"Has ganado. Tienes {cantidad} euros ahora")
    if miMoneda != resultadoMonedaAleatoria:
        cantidad = cantidad - 100
        print(f"Has perdido. Tienes {cantidad} euros ahora")
    jugadas += 1
print(f"Has jugado {jugadas-1} veces")
