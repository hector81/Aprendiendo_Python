def introducirNumero():
     while True:
         try:
             numero = int(input("Por favor ingrese el número de CCAA: "))
             return numero
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def devolverProvincias_PorNumeroCCAA(numero,arrayCCAA_Provincias):
    arrayPROV = []
    # para recorrer las ccaa
    for i in range(len(arrayCCAA_Provincias)):
        if i+1 == numero:
            print('Has elegido ' + str(arrayCCAA_Provincias[i][0]))
            arrayPROV.append(arrayCCAA_Provincias[i][1])

    # para recorrer las provincias
    for i in range(len(arrayPROV)):
        for j in range(len(arrayPROV[i])):
            print(str(j+1) + ' = ' + arrayPROV[i][j])


#####################fin funcion ################

arrayCCAA_Provincias = [
        ['Andalucía',['Almería','Cádiz','Córdoba','Granada','Huelva','Jaén','Málaga','Sevilla']],
        ['Aragón',['Huesca','Zaragoza','Teruel']],
        ['Canarias',['Las Palmas','Santa Cruz de Tenerife']],
        ['Cantabria',['Cantabria']],
        ['Castilla y León',['Avila','Burgos','León','Palencia','Salamanca','Segovia','Soria','Valladolid','Zamora']],
        ['Castilla-La Mancha',['Albacete','Ciudad Real','Cuenca','Guadalajara','Toledo']],
        ['Cataluña',['Barcelona','Gerona','Lérida','Tarragona']],
        ['Ceuta',['Ceuta']],
        ['Comunidad Valenciana',['Alicante','Castellón','Valencia']],
        ['Comunidad de Madrid',['Madrid']],
        ['Extremadura',['Badajoz','Cáceres']],
        ['Galicia',['La Coruña','Lugo','Orense','Pontevedra']],
        ['Islas Baleares',['Islas Baleares']],
        ['La Rioja',['La Rioja']],
        ['Melilla',['Melilla']],
        ['Navarra',['Navarra']],
        ['País Vasco',['Alava','Guipúzcoa','Vizcaya']],
        ['Principado de Asturias',['Asturias']],
        ['Región de Murcia',['Murcia']]
    ]


print('Elige la CCAA que quieres para ver sus provincias. Pon el numero')
for i in range(len(arrayCCAA_Provincias)):
        print(str(i+1) + ' = '  + arrayCCAA_Provincias[i][0])

numero = introducirNumero()
devolverProvincias_PorNumeroCCAA(numero,arrayCCAA_Provincias)
