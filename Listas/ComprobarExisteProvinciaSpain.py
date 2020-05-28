def comprobarExisteProvincia(nombre):
    arrayProvincias = ['Alava','Albacete','Alicante','Almería','Asturias','Avila','Badajoz','Barcelona','Burgos','Cáceres',
    'Cádiz','Cantabria','Castellón','Ciudad Real','Córdoba','La Coruña','Cuenca','Gerona','Granada','Guadalajara',
    'Guipúzcoa','Huelva','Huesca','Islas Baleares','Jaén','León','Lérida','Lugo','Madrid','Málaga','Murcia','Navarra',
    'Orense','Palencia','Las Palmas','Pontevedra','La Rioja','Salamanca','Segovia','Sevilla','Soria','Tarragona',
    'Santa Cruz de Tenerife','Teruel','Toledo','Valencia','Valladolid','Vizcaya','Zamora','Zaragoza']

    nombreBuscar = nombre.upper()
    posicion = ''
    boolComp = False
    for i in range(len(arrayProvincias)):
        posicion = arrayProvincias[i].upper()
        if posicion == nombreBuscar:
            boolComp = True

    if boolComp == True:
        print('La provincia existe en España')
    else:
        print('La provincia no existe en España')

def introducirPalabra():
     while True:
         try:
             nombre = input("Por favor ingrese una nombre de provincia: ")
             if nombre != '':
                 print("El nombre de provincia es " + nombre)
                 return nombre
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


nombre = introducirPalabra()
comprobarExisteProvincia(nombre)
