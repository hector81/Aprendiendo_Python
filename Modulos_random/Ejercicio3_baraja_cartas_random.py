'''
EJERCICIOS
MÓDULO random
3. Suponga una baraja de 10 cartas. Cada una tiene un número que va del 1 al 10. Baraje
 y reparta 5 para usted y 5 para el ordenador. Muestre su jugada y la del ordenador.
 Gana el que obtenga mayor puntuación. Imprima el ganador. En caso de empate,
 juegue de nuevo. NOTA: No puede repartir una carta que ya haya sido repartida.
'''
import random
# FUNCIONES
def comprobarCartasNumeros_repetidos(numero1,numero2):
    comp = False
    if numero1 == numero2:
        comp = True
    return comp

def borrarCartas(numero1,numero2,barajaLista):
    #borramos por su valor
    barajaLista.remove(numero1)
    barajaLista.remove(numero2)

def comprobarRepetidosListaNumero(lista , numero1, numero2):
    comp = False
    for elemento in lista:
        if elemento == numero1 or elemento == numero2:
            comp = True
    return comp

# VARIABLES
jugadas = 0
miJugada = 0
jugadaOrdenador = 0
barajaLista = [1,2,3,4,5,6,7,8,9,10]
baraja_numeros_ya_jugados = []

# OPERACIONES
while jugadas < 5:
    cartaMia = random.randint(1, 10)
    cartaOrdenador = random.randint(1, 10)
    # si las cartas no están repetidas o no sean iguales
    if(comprobarCartasNumeros_repetidos(cartaMia,cartaOrdenador)) == False:
        # comprobamos que no esten en los que ya han sido jugados
        if comprobarRepetidosListaNumero(baraja_numeros_ya_jugados , cartaMia, cartaOrdenador) == False:
            # los añadimos a los numeros ya jugados
            baraja_numeros_ya_jugados.append(cartaMia)
            baraja_numeros_ya_jugados.append(cartaOrdenador)
            print(f"Jugada {jugadas+1}. Tu carta es {cartaMia} y la del ordenador es {cartaOrdenador}")
            # borramos las cartas
            borrarCartas(cartaMia,cartaOrdenador,barajaLista)
            if cartaMia > cartaOrdenador:
                print(f"Gano yo")
                jugadas += 1
            elif cartaMia < cartaOrdenador:
                print(f"Gana el ordenador")
                jugadas += 1
    else:
        print(f"Empate. Las cartas se devuelven a la baraja")
