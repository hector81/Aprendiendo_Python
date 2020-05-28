nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linea = ''
for i in nums:
    for y in nums:
        linea = linea + str(i*y) + ' '
    linea = linea + '\n'
print(linea)
