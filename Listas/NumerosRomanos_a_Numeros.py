# https://devcode.la/tutoriales/diccionarios-en-python/
# https://jarroba.com/diccionario-python-ejemplos/

def introducirNumeroInt():
    while True:
        try:
            x = int(input("Por favor ingrese un número del 1 al 3999: "))
            if x > 0 and x < 4000:
                return x
                break
            else:
                print("Por favor. Un número del 1 al 3999")
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")
# fin funcion

def convertirPorLetraNumero(posicion, numStr):
    letra = ""
    for i in range(len(numRomaUnidades)):
        if i == posicion:
            diccionario = numRomaUnidades[i]
            for key in diccionario:
                if key == numStr:
                    letra = diccionario[key]
    return letra

def transformarNumeros_A_Romanos(numero,numRomaUnidades):
    # avergiuamdos su longitud
    numeroSTR = str(numero)

    numeroRomano = ""
    numeroSTReves = numeroSTR[:: -1]
    for i in range(len(numeroSTReves)):
        numeroRomano = convertirPorLetraNumero(i, numeroSTReves[i]) + numeroRomano

    print(numeroRomano)


numRomaUnidades = {
    0 : { "0": "", "1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII", "9": "IX" }, # unidades
    1 : { "0": "", "1": "X", "2": "XX", "3": "XXX", "4": "XL", "5": "L", "6": "LX", "7": "LXX", "8": "LXXX", "9": "XC" },# decenas
    2 : { "0": "", "1": "C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6": "DC", "7": "DCC", "8": "DCCC", "9": "CM" },# centenas
    3 : { "0": "", "1": "M", "2": "MM", "3": "MMM" } # millares
}

# Con upper() la letra siempre sera pasada a mayuscula
numero = introducirNumeroInt()
transformarNumeros_A_Romanos(numero,numRomaUnidades)
