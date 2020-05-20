'''
4. Lee una cadena de texto del usuario y para cada letra indica si es una vocal o una consonante.
'''
cadenaTexto = "Esto es una cadena de texto de prueba"
listaVocales = ["a","e","i","o","u"]

for letra in cadenaTexto:
    if letra != " ":
        if letra.lower() in listaVocales:
            print(f"{letra} es vocal")
        else:
            print(f"{letra} es consonante")
    else:
        print(f"***********")
