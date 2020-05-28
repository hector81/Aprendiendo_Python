def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


introducirNumero()
