palabra = input("Pon la palabra = ")

palabraVuelta = palabra[:: -1]

print("La palabra vuelta es " + palabraVuelta)


if palabraVuelta == palabra:
    print(palabra + " es palindroma")
else:
    print(palabra + " no es palindroma")
