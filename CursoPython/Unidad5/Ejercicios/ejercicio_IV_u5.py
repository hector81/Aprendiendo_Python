'''

En unas oposiciones el reparto de aulas se realiza en función de la letra del DNI, así que a partir 
del numero del DNI debemos calcular la letra y en función de la posición de esa letra en la secuencia 
del algoritmo debe ser enviado a un aula o a otra.

Para las letras que estén:

entre la posición 0 y 5 al aula 1
entre la posición 6 y 11 aula 2
entre la posición 12 y 17 aula 3
entre la posición 18 y 22 aula 4
Paso a paso:

Paso 1: Solicitamos a usuario el número del DNI.
Paso 2: Definimos el string que contiene la secuencia de letras utilizadas en el 
algoritmo: TRWAGMYFPDXBNJZSQVHLCKE.
Paso 3: Calculamos y guardamos la posición de la letra dentro del string que se calcula 
obteniendo el resto, módulo o resíduo de dividir el DNI entre 23. El resto varia entre 0, 
que supone división exacta, y 22.
Paso 4: Consultamos la palabra para ver el caracter que corresponde.
Ejemplo si el resto es cero corresponde una T y si es 22 corresponde una E.
Paso 5: Realizamos todas las comprobaciones para saber en que posición está la letra y en 
función de esto enviarlo a un aula o a otra
'''

numero_dni = float(input("Escribe tu número de DNI: ")) 

diccionario_letras = {0:"T" ,1:"R" ,2:"W" ,3:"A" ,4:"G" ,5:"M" ,6:"Y" ,7:"F" ,8:"P" ,9:"D" ,10:"X"
 ,11:"B" ,12:"N" ,13:"J" ,14:"Z" ,15:"S" ,16:"Q" ,17:"V" ,18:"H" ,19:"L" ,20:"C" ,21:"K" ,22:"E"}

posicion_letra = int(numero_dni%23)

print(f"La letra de tu DNI es {diccionario_letras[posicion_letra]} y tu posicion es {posicion_letra}")

if posicion_letra > -1 and posicion_letra < 6:
    print(f"El aula que te corresponde es el aula 1") # entre la posición 0 y 5 al aula 1
elif posicion_letra > 5 and posicion_letra < 12:
    print(f"El aula que te corresponde es el aula 2") # entre la posición 6 y 11 aula 2
elif posicion_letra > 11 and posicion_letra < 18:
    print(f"El aula que te corresponde es el aula 3") # entre la posición 12 y 17 aula 3
else:
    print(f"El aula que te corresponde es el aula 4") # entre la posición 18 y 22 aula 4


