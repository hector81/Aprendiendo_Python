'''
1. Lee una cadena de texto del usuario e imprime por pantalla un mensaje simpatico si y
solo si la cadena es un palíndromo (se lee igual de izquierda a derecha que de derecha
a izquierda). Algunos ejemplos: La ruta natural ¿Son mulas o cívicos alumnos?
Dábale arroz a la zorra el abad
'''

frase1 = "Son mulas o cívicos alumnos"
frase2 = "Dabale arroz a la zorra el abad"

def volverFaseReves(frase):
    print(frase)
    # separamos
    listaA = frase.split(" ")
    listaB = frase.split(" ")
    listaB.reverse()
    listaC = []
    for palabra in listaB:
        listaC.append(palabra[:: -1])

    listaStringA = "".join(listaA).lower()
    listaStringB = "".join(listaC).lower()

    if listaStringA == listaStringB:
        print("Es palindroma. Esto es un mensaje simpático")
    else:
        print(f"No es palindroma")

volverFaseReves(frase1)
volverFaseReves(frase2)
