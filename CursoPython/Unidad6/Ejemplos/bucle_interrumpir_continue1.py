def esPrimo(n):
    divisor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisor = divisor + 1
    if divisor == 2:
        return True
    else:
        return False

    
for num in range(2, 100):
    if esPrimo(num):
        print("PRIMO = ", num)
        continue
    print(num)