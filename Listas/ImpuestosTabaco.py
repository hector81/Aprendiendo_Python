# funciones
def introducirNumero():
     while True:
         try:
             numero = int(input("Por favor ingrese el número de cajetilla de tabaco "))
             return numero
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def leerPreciosTabaco(arrayPreciosTabaco):
    for i in range(len(arrayPreciosTabaco)):
        print(str(i+1) + ' - Cajetilla ' + str(arrayPreciosTabaco[i][0]) + '. Precio = ' + str(arrayPreciosTabaco[i][1]) + ' €.')

def calcularImpuestos(arrayPreciosTabaco, numero, impuestos):
    nombre = ''
    precio = 0.0
    for i in range(len(arrayPreciosTabaco)):
        if i == (numero - 1):
            nombre = arrayPreciosTabaco[i][0]
            precio = arrayPreciosTabaco[i][1]
    print('El impuesto actual del tabaco es el ' + str(impuestos) + ' %')
    print('Has elegido ' + nombre + ' y su precio es ' + str(precio) + ' €, de los cuales ' + str((precio*impuestos)/100) + ' € son impuestos y el resto ' + str( precio - (precio*impuestos)/100) + ' € es lo que vale realmente el tabaco')

arrayPreciosTabaco = [
    ['Fortuna',4.70],
    ['Elixyr',4.10],
    ['Herencia',5.00],
    ['L&M',4.25],
    ['Lucky Strike',4.50],
    ['Marlboro',5.00],
    ['Pall Mall',4.45],
    ['Philip Morris',4.15],
    ['West',4.15],
    ['Winston',4.40],
    ['Ducados Rubio',4.25],
    ['Desert Gold',4.00],
    ['Camel',4.60],
    ['Ducados Negro',5.45]
]

impuestos = float(78.8)

# operaciones
leerPreciosTabaco(arrayPreciosTabaco)
numero = introducirNumero()
calcularImpuestos(arrayPreciosTabaco, numero, impuestos)
