'''
Escriba un programa que resuelva el siguiente problema:
El índice de masa corporal IMC de una persona se calcula con la fórmula IMC=P/T2 en donde P es 
el peso en Kg. y T es la talla en metros.

Reciba un valor de P y de T, calcule el IMC y muestre su estado  según la siguiente tabla:  

IMC	            Estado
Menos de 18.5	Desnutrido
18.5 a 25.5	    Peso óptimo
Más de 25.5	    Sobrepreso
'''
p = float(input("Escribe el valor de P: ")) # peso
t = float(input("Escribe el valor de T: "))  # altura
imc = p/t**2
if imc < 18.5:
    print(f"Tú índice de masa corporal IMC es {imc} y tu estado es desnutrido.")
elif imc >= 18.5 and imc <= 25.5:
    print(f"Tú índice de masa corporal IMC es {imc} y tu estado es peso óptimo.")
else:
    print(f"Tú índice de masa corporal IMC es {imc} y tu estado es sobrepreso.")