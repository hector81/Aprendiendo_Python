
for i in range(1, 11):
    print("Tabla del " + str(i))
    for j in range(1, 11):
        if (i*j)%2==0:
            print(i*j, end=" PAR \t")
        else:
            print(i*j, end=" IMPAR \t")
    print("")
