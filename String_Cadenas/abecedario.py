arrayAbecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','y','z'];

def introducirLetra():
     while True:
         try:
             letra = input("Por favor ingrese una letra: ")
             if len(letra) == 1:
                 print("La letra es " + letra)
                 return letra
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


letra = introducirLetra()
for i in range(len(arrayAbecedario)):
    if letra == arrayAbecedario[i]:
        print('La letra ' + letra + ' está en el abecedario en la posición ' + str(i+1))
