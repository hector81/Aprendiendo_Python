'''
Escribe un programa que resuelva el siguiente problema.
Reciba por teclado dos números y determinar si la suma de ambas cifras es un número par o impar.
Muéstralo en un mensaje
'''
numero1 = int(input("Pon el primer número para sumar: "))
numero2 = int(input("Pon el segundo número para sumar: "))
suma = numero1 + numero2

if suma%2 == 0:
    print(f"La suma de {numero1} y {numero2} es {suma} y por lo tanto PAR")
else:
    print(f"La suma de {numero1} y {numero2} es {suma} y por lo tanto IMPAR")
    