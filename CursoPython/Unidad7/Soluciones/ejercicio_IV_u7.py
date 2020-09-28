def fibonacci(n):
    """ Generador de números Fibonacci """
    a, b, contador = 0, 1, 0
    while True:
        if (contador > n): 
            return
        yield a
        a, b = b, a + b
        contador += 1
f = fibonacci(15)
for x in f:
    print(x) # 
print()