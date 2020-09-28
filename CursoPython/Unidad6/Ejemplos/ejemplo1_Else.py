n = int(input('Ingresa un número y te digo si es primo. '))
for x in range(2,n):
    if n % x == 0:
        print(n, 'es igual a', x, '*', n/x)
        break
else:
    print(n, 'es un número primo')

'''
Condicional con if para saber si un número no es primo.

En caso de que la condición sea verdadera (no primo), se ejecuta un print avisando del hecho y sale del 
bucle con la sentencia break.

En caso contrario, es decir, que la condición no sea verdad se ejecutará el contenido identado dentro de else.



La instrucción "else" después de un ciclo solo tiene sentido cuando se usa en combinación con break.
 Si durante la ejecución del bucle, el intérprete de Python encuentra un break, inmediatamente detiene 
 la ejecución del bucle y sale de él. En este caso, la rama else: no se ejecuta.

Básicamente, la sentencia else está conectada al bucle y cuando el bucle no tiene interrupción
 (lo que significa que la sentencia break no es usada) lo que está bajo la sentencia else se ejecuta.
'''