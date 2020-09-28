for num in range(2, 10):
    if num % 2 == 0:
        print("Número par", num)
        pass #sentencia que indica que deberemos incrustar más contenido pero está sin definir
    print("Número impar", num)

cadena = "Número impares "
print(cadena)
for num in range(2, 10):
    if num % 2 == 0:
        pass #sentencia que indica que deberemos incrustar más contenido pero está sin definir
    else:
        print(num, end = ' ')