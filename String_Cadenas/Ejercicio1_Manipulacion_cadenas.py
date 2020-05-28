'''
Manipulación de cadenas utilizando el intérprete:
'''
cadena = "Cabeza grande, ojos hermosos"
print(f"Cadena = {cadena}")
print(f"1. ¿El tamaño de la cadena?")
print(len(cadena))
print(f"2. Los primeros cinco caracteres de la cadena.")
print(cadena[0:5])
print(f"3. Los siete últimos caracteres.")
print(cadena[len(cadena)-7:len(cadena)])
print(f"4. Los cinco primeros caracteres, de dos en dos.")
print(cadena[0:5:2])
print(f"5. Los últimos trece caracteres, de tres en tres.")
print(cadena[len(cadena)-13:len(cadena):3])
print(f"6. En mayúscula, los caracteres en posiciones múltiplo de tres.")
print(cadena[3:len(cadena):3].upper())
print(f"7. De dos en dos, del caracter en la posición 4 al de la 17.")
print(cadena[4:17:2])
print(f"8. ¿Está el caracter 'x' en la cadena?")
resultadoBusquedaX = cadena.find('x')
if resultadoBusquedaX != -1:
    print("El caracter x está")
else:
    print("El caracter x no está")
print(f"9. ¿Y 'o', en mayúscula o minúscula?")
resultadoBusquedaO = cadena.find('O')
if resultadoBusquedaO != -1:
    print("El caracter O está")
else:
    print("El caracter O no está")
resultadoBusquedao = cadena.find('o')
if resultadoBusquedao != -1:
    print("El caracter o está")
else:
    print("El caracter o no está")
