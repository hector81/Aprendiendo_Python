#http://progra.usm.cl/apunte/ejercicios/2/autores-libros.html
from datetime import datetime, date, timedelta
def obtener_idioma(titulo):
    autor = ''
    for i in range(len(libros)):
        if titulo in libros[i]:
            autor = libros[i][1]
    idioma = datos_autores[autor][2]
    return idioma

def obtener_autor(titulo):
    autor = ''
    for i in range(len(libros)):
        if titulo in libros[i]:
            autor = libros[i][1]
    return autor

def calcular_annos_antes_de_morir(titulo):
    fechaNacimiento = ()
    fechaDefuncion = ()
    for i in range(len(libros)):
        if titulo in libros[i]:
            autor = libros[i][1]
    fechaNacimiento = datos_autores[autor][0]
    fechaDefuncion = datos_autores[autor][1]

    nacimientoDate = datetime(fechaNacimiento[0], fechaNacimiento[1], fechaNacimiento[2], 0, 0, 00, 00000)
    defuncionDate = datetime(fechaDefuncion[0], fechaDefuncion[1], fechaDefuncion[2], 0, 0, 00, 00000)

    # primero restamos el año
    edad = int(defuncionDate.year) - int(nacimientoDate.year)
    ''' esto es por si es menos de 1 año la diferencia '''
    if defuncionDate.month >  nacimientoDate.month:
        edad = edad
    elif defuncionDate.month <  nacimientoDate.month:
        edad = edad - 1
    elif defuncionDate.month ==  nacimientoDate.month:
        if defuncionDate.day >  nacimientoDate.day:
            edad = edad
        elif defuncionDate.day <  nacimientoDate.day:
            edad = edad -1
        elif defuncionDate.day ==  nacimientoDate.day:
            edad = edad

    return edad

def devolverFechaDefuncion(titulo):
    fechaNacimiento = ()
    fechaDefuncion = ()
    for i in range(len(libros)):
        if titulo in libros[i]:
            autor = libros[i][1]
    fechaDefuncion = datos_autores[autor][1]

    return str(fechaDefuncion[2]) + '-' + str(devolverMesPorNumero(fechaDefuncion[1])) + '-' + str(fechaDefuncion[0])

def devolverFechaNacimiento(titulo):
    fechaNacimiento = ()
    fechaDefuncion = ()
    for i in range(len(libros)):
        if titulo in libros[i]:
            autor = libros[i][1]
    fechaNacimiento = datos_autores[autor][0]

    return str(fechaNacimiento[2]) + '-' + str(devolverMesPorNumero(fechaNacimiento[1])) + '-' + str(fechaNacimiento[0])

def devolverMesPorNumero(numero):
    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    mes = meses[numero-1]
    return mes

libros = [
    ('Papelucho programador', 'Marcela Paz', 1983),
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', 1615),
    ('Romeo y Julieta', 'William Shakespeare', 1597),
    ('La metamorfosis', 'Franz Kafka', 1915),
    # ...
]

datos_autores = {
    # autor: nacimiento, defuncion, idioma
    'William Shakespeare': ((1564,  4, 26), (1616,  5,  3), 'inglés'),
    'Franz Kafka':         ((1883,  7,  3), (1924,  6,  3), 'alemán'),
    'Marcela Paz':         ((1902,  2, 28), (1985,  6, 12), 'español'),
    'Miguel de Cervantes': ((1547,  9, 29), (1616,  4, 22), 'español'),
    # ...
}

titulo = input('Ingrese titulo del libro: ')
print('El libro fue escrito en ' + obtener_idioma(titulo))
print('por ' + obtener_autor(titulo))
print('El autor fallecio con ' + str(calcular_annos_antes_de_morir(titulo)) + ' años')
print('después de haber escrito el libro')
print('Pues había nacido el ' + devolverFechaNacimiento(titulo) + ' y su fecha de defunción se produjo el ' + devolverFechaDefuncion(titulo))
