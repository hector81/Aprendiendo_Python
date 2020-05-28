a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print("posicion i = " + str(i) + " | posicion j = " + str(j) + " .Igual a =" + str(a[i][j]))
    print()

print()

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
