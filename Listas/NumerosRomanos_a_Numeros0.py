# https://devcode.la/tutoriales/diccionarios-en-python/
# https://jarroba.com/diccionario-python-ejemplos/
# OPERACIONES
def introducirPalabra():
     while True:
         try:
             palabra = input("Por favor ingrese una numeración romana: ")
             if palabra != '':
                 palabraM = palabra.upper()
                 if comprobarLetrasNumerosRomanos(palabraM) == True:
                     print("El número es " + palabraM)
                     return palabra
                     break
                 else:
                     print("Alguna letra no coincide con la numeración romana")
             else:
                 print("La numeración está vacia")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def comprobarLetraEsNumeroRomano(letra):
    numerosRomanos = ["I","V","X","L","C","D","M"]
    boolComp = False
    contador = 0
    for i in range(len(numerosRomanos)):
        if letra == numerosRomanos[i]:
            boolComp = True
    return boolComp

def comprobarLetrasNumerosRomanos(numeroRomano):
    letraFalsa = False
    for i in range(len(numeroRomano)):
        letraFalsa = comprobarLetraEsNumeroRomano(numeroRomano[i])
    return letraFalsa

def transformarNumeros_A_Romanos(numeroRomano):
    contador = 0
    for i in range(len(numeroRomano)):
        if numeroRomano[i] == 'M':
    print('EL NÚMERO ES' + contador)

# VARIABLES


numRomaUnidades = {
    0 : { "0": "", "1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII", "9": "IX" }, # unidades
    1 : { "0": "", "1": "X", "2": "XX", "3": "XXX", "4": "XL", "5": "L", "6": "LX", "7": "LXX", "8": "LXXX", "9": "XC" },# decenas
    2 : { "0": "", "1": "C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6": "DC", "7": "DCC", "8": "DCCC", "9": "CM" },# centenas
    3 : { "0": "", "1": "M", "2": "MM", "3": "MMM" } # millares
}
# OPERACIONES

numeroRomano = introducirPalabra()
#transformarNumeros_A_Romanos(numeroRomano)
