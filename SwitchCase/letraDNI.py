def devolverLetra(numeroDni):
    restoNIF = 0
    numeroDNInt = int(numeroDni)
    restoNIF = numeroDNInt%23

    if restoNIF == 0:
        print("La letra es la T")
    elif restoNIF == 1:
        print("La letra es la R")
    elif restoNIF == 2:
        print("La letra es la W")
    elif restoNIF == 3:
        print("La letra es la A")
    elif restoNIF == 4:
        print("La letra es la G")
    elif restoNIF == 5:
        print("La letra es la M")
    elif restoNIF == 6:
        print("La letra es la Y")
    elif restoNIF == 7:
        print("La letra es la F")
    elif restoNIF == 8:
        print("La letra es la P")
    elif restoNIF == 9:
        print("La letra es la D")
    elif restoNIF == 10:
        print("La letra es la X")
    elif restoNIF == 11:
        print("La letra es la B")
    elif restoNIF == 12:
        print("La letra es la N")
    elif restoNIF == 13:
        print("La letra es la J")
    elif restoNIF == 14:
        print("La letra es la Z")
    elif restoNIF == 15:
        print("La letra es la S")
    elif restoNIF == 16:
        print("La letra es la Q")
    elif restoNIF == 17:
        print("La letra es la V")
    elif restoNIF == 18:
        print("La letra es la H")
    elif restoNIF == 19:
        print("La letra es la L")
    elif restoNIF == 20:
        print("La letra es la C")
    elif restoNIF == 21:
        print("La letra es la K")
    elif restoNIF == 22:
        print("La letra es la E")



numero = 0
numeroDni = ''
restoNIF = 0
comp = False
while numero != 8 and comp == False:
    numeroDni = input("Pon tu numero de dni para averiguar tu letra = ")
    comp = numeroDni.isdigit()
    numero = len(numeroDni)
    if numero != 8 or comp == False:
        print("El numero debe tener 8 numeros y no puede tener letras")
        numero = 0
    else:
        print("El numero es correcto")
        devolverLetra(numeroDni)
