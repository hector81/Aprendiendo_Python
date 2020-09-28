"""paquete del moulo principal del descuento"""

import random


def sorteo(valor):

    x = random.choice([0,10,20,25,50])

    bolas = {0:"BOLA BLANCA", 10:"BOLA ROJA", 20:"BOLA AZUL", 25:"BOLA VERDE", 50:"BOLA AMARILLA"}    
    
    if x == 0:
        print("Lo siento no tienes descuento, te salió la bola blanca")
    else:
        la_bola = bolas[x]
        a_pagar = float (valor -(float(valor * x)/100))
        print(f"Has sacado una bola {la_bola}")
        print(f"Felicidades tienes un {x}% de descuento")
        print(f"Debes pagar: {a_pagar}")

def promocion(): #Información del descuento
    print ("")
    print ("Has gastado al menos 100.00€, Ahora participa en el sorteo para la promoción.")
    print ("")
    print ("  COLOR            DESCUENTO")
    print ("")
    print ("  BOLA BLANCA     NO TIENE DESCUENTO")
    print ("  BOLA ROJA       10 POR CIENTO")
    print ("  BOLA AZUL       20 POR CIENTO")
    print ("  BOLA VERDE      25 POR CIENTO")
    print ("  BOLA AMARILLA   50 POR CIENTO")
    print ("")


def cobro():
    
    cobra =  float(input("Cuanto ha gastado el cliente?? "))

    if cobra < 100.00:
        print("Lo siento pero no se te aplica el descuento")
    else:
        print("Se te aplicará un descuento dependiendo del sorteo")
        promocion()
        input("Para ejecutarlo pulsa en intro...")
        sorteo(cobra)