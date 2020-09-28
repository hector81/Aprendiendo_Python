n = int(input('Introduce un número mayor que 1: '))
if n <= 1:
    print('Eso no es un número mayor que 1 :(')
else:
    divisor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisor = divisor + 1
    if divisor == 2:
        print('Pues si, es primo')
    else:
        print('Pues no, no es primo, tiene ',divisor, ' divisores.')