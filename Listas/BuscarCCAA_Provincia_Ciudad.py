def introducirNumero(variable):
     while True:
         try:
             numero = int(input("Por favor ingrese el número de " + variable + " : "))
             return numero
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def devolverProvincias_Ciudad_PorNumeroCCAA(numero,arrayCCAA_Provincias):
    arrayPROV = []
    # para recorrer las ccaa
    for i in range(len(arrayCCAA_Provincias)):
        if i+1 == numero:
            print('Has elegido ' + str(arrayCCAA_Provincias[i][0]))
            arrayPROV.append(arrayCCAA_Provincias[i][1])

    arrayMun = []
    # para recorrer las provincias
    for i in range(len(arrayPROV)):
        for j in range(len(arrayPROV[i])):
            arrayMun.append(arrayPROV[i][j])
            print(str(j+1) + ' = ' + arrayPROV[i][j][0])

    numeroProv = introducirNumero('provincia')

    capital = []

    arrayLoc = []
    # para recorrer las municipios con capitales
    for i in range(len(arrayMun)):
        if i == numeroProv-1:
            print('Has elegido ' + str(arrayMun[i][0]))
            capital = arrayMun[i][1]
            arrayLoc.append(arrayMun[i][2])

    for i in range(len(capital)):
        print(capital[i])

    print('Sus localidad o poblaciones son : ')
    arrayMun = []
    for i in range(len(arrayLoc)):
        arrayMun = arrayLoc[i]

    for i in range(len(arrayMun)):
        print((str(i+1) + ' = ' + arrayMun[i]))
#####################fin funcion ################


# array variable global
arrayCCAA_Provincias = [
        ['Andalucía',
            [
                ['Almería',
                    ['Su capital es Almería',
                        ['Abla','Abrucena','Adra','Alboloduy','Albox','Albánchez','Almería']
                    ]
                ],
                ['Cádiz',
                    ['Su capital es Cádiz'],
                        ['Cádiz','Chiclana de la Frontera','Zahara de la Sierra']
                ],
                ['Córdoba',
                    ['Su capital es Córdoba'],
                        ['Aguilar de la Frontera','Córdoba','Valenzuela']
                ],
                ['Granada',
                    ['Su capital es Granada'],
                        ['Albuñuelas','Almegíjar','Alpujarra de la Sierra','Granada']
                ],
                ['Huelva',
                    ['Su capital es Huelva'],
                        ['Aljaraque','Aroche','Berrocal','Huelva']
                ],
                ['Jaén',
                    ['Su capital es Jaén'],
                        ['Alcalá la Real','Arjona','Cambil','Jaén']
                ],
                ['Málaga',
                    ['Su capital es Málaga'],
                        ['Alhaurín de la Torre','Cártama','Málaga','Ronda']
                ],
                ['Sevilla',
                    ['Su capital es Sevilla'],
                        ['Aguadulce','Alanís','Algámitas','Sevilla']
                ]
            ]
        ],
        ['Aragón',
            [
                ['Huesca',
                    ['Su capital es Huesca'],
                        ['Albalatillo','Castigaleu','Huesca','Huesca']
                ],
                ['Zaragoza',
                    ['Su capital es Zaragoza'],
                        ['Gelsa','Marracos','Orcajo','Zaragoza']
                ],
                ['Teruel',
                    ['Su capital es Teruel'],
                        ['Ababuj','Alba','Alcañiz','Teruel']
                ]
            ]
            ],
        ['Canarias',
            [
                ['Las Palmas',
                    ['Su capital es Las Palmas'],
                        ['El Hierro‎','La Gomera‎','Las Palmas','Tenerife']
                ],
                ['Santa Cruz de Tenerife',
                    ['Su capital es  Santa Cruz de Tenerife'],
                        ['El Hierro‎','La Gomera‎','Las Palmas','Tenerife']
                ]
            ]
        ],
        ['Cantabria',
            [
                ['Cantabria',
                    ['Su capital es Santander'],
                        ['Cabezón de Liébana','Los Corrales de Buelna','Herrerías','Santander']
                ]
            ]
        ],
        ['Castilla y León',
            [
                ['Avila',
                    ['Su capital es Avila'],
                        ['Adanero','Avila','Bonilla de la Sierra','Cabezas de Alambre']
                ],
                ['Burgos',
                    ['Su capital es Burgos'],
                        ['Abajas','Alfoz de Bricia','Burgos','Cabañes de Esgueva']
                ],
                ['León',
                    ['Su capital es León'],
                        ['Cubillos del Sil','La Ercina‎','Escobar de Campos','León']
                ],
                ['Palencia',
                    ['Su capital es Palencia'],
                        ['Espinosa de Cerrato','Fuentes de Valdepero','Itero de la Vega','Palencia']
                ],
                ['Salamanca',
                    ['Su capital es Salamanca'],
                        ['La Alameda de Gardón','La Alameda de Gardón','Aldea del Obispo','Salamanca']
                ],
                ['Segovia',
                    ['Su capital es Segovia'],
                        ['Fresneda de Cuéllar','Grajera','Hontanares de Eresma','Segovia']
                ],
                ['Soria',
                    ['Su capital es Soria'],
                        ['Abejar','Las Aldehuelas','Nepas','Soria']
                ],
                ['Valladolid',
                    ['Su capital es Valladolid'],
                        ['Adalia','Amusquillo','Bahabón','Valladolid']
                ],
                ['Zamora',
                    ['Su capital Zamora'],
                        ['Abezames','Arcos de la Polvorosa','Calzadilla de Tera','Zamora']
                ]
            ]
        ],
        ['Castilla-La Mancha',
            [
                ['Albacete',
                    ['Su capital es Albacete'],
                        ['Abengibre','Albacete','Balazote','Balsa de Ves']
                ],
                ['Ciudad Real',
                    ['Su capital es Ciudad Real'],
                        ['Alcubillas','Brazatortas','Ciudad Real','Fuente el Fresno']
                ],
                ['Cuenca',
                    ['Su capital es Cuenca'],
                        ['Abia de la Obispalía','Alcalá de la Vega','Cuenca','Fresneda de Altarejos']
                ],
                ['Guadalajara',
                    ['Su capital es Guadalajara'],
                        ['Alcolea del Pinar‎','Budia‎','Castilnuevo','Guadalajara']
                ],
                ['Toledo',
                    ['Su capital es '],
                        ['Borox‎','Menasalbas','San Martín de Montalbán‎','Toledo']
                ]
            ]
        ],
        ['Cataluña',
            [
                ['Barcelona',
                    ['Su capital es Barcelona'],
                        ['Barcelona','Ripollet','Sabadell','Sitges']
                ],
                ['Gerona',
                    ['Su capital es Gerona'],
                        ['Bañolas‎','Llagostera‎','Gerona','Lloret de Mar‎','assanas']
                ],
                ['Lérida',
                    ['Su capital es Lérida'],
                        ['Abella de la Conca','Borjas Blancas','Castellbó','Lérida']
                ],
                ['Tarragona',
                    ['Su capital es Tarragona'],
                        ['Alió','Cabacés','Freginals','Tarragona']
                ]
            ]
        ],
        ['Ceuta',
            [
                ['Ceuta',
                    ['Su capital es Ceuta'],
                        ['Ceuta']
                ]
            ]
        ],
        ['Comunidad Valenciana',
            [
                ['Alicante',
                    ['Su capital es Alicante'],
                        ['Alicante','Benejama','Callosa de Segura‎','Finestrat‎']
                ],
                ['Castellón',
                    ['Su capital es Castellón de la Plana'],
                        ['Adzaneta‎','Benicasim‎','Castellón de la Plana','Fanzara‎']
                ],
                ['Valencia',
                    ['Su capital es Valencia'],
                        ['Albaida‎','Alfafar','Bellreguart','Valencia']
                ]
            ]
        ],
        ['Comunidad de Madrid',
            [
                ['Madrid',
                    ['Su capital es Madrid'],
                        ['Madrid','Mostoles','Navalcarnero','Parla']
                ]
            ]
        ],
        ['Extremadura',
            [
                ['Badajoz',
                    ['Su capital es Badajoz'],
                        ['Alange‎','Badajoz','Burguillos del Cerro‎','Fregenal de la Sierra']
                ],
                ['Cáceres',
                    ['Su capital es Cáceres'],
                        ['Alcántara','Cáceres','Hinojal‎','Ibahernando‎']
                ]
            ]
        ],
        ['Galicia',
            [
                ['La Coruña',
                    ['Su capital es La Coruña'],
                        ['Aranga','La Coruña','Mellid','Mesía']
                ],
                ['Lugo',
                    ['Su capital es Lugo'],
                        ['Abadín','Baleira','Lugo','Muras']
                ],
                ['Orense',
                    ['Su capital es Orense'],
                        ['Allariz','Arnoya','Orense','Porquera']
                ],
                ['Pontevedra',
                    ['Su capital es Pontevedra'],
                        ['Nigrán‎','Pontevedra‎','Redondela‎','Vigo']
                ]
            ]
        ],
        ['Islas Baleares',
            [
                ['Islas Baleares',
                    ['Su capital es Palma de Mallorca'],
                        ['Formentera','Mahón','Palma de Mallorca','illacarlos']
                ]
            ]
        ],
        ['La Rioja',
            [
                ['La Rioja',
                    ['Su capital es Logroño'],
                        ['Haro','Lardero','Logroño','Munilla']
                ]
            ]
        ],
        ['Melilla',
            [
                ['Melilla',
                    ['Su capital es Melilla'],
                        ['Melilla']
                ]
            ]
        ],
        ['Navarra',
            [
                ['Navarra',
                    ['Su capital es Pamplona'],
                        ['Azagra','Baztán‎','Estella','Pamplona']
                ]
            ]
        ],
        ['País Vasco',
            [
                ['Alava',
                    ['Su capital es Vitoria'],
                        ['Alegría de Álava','Aramayona','Cripán','Lanciego','Oyón','Vitoria']
                ],
                ['Guipúzcoa',
                    ['Su capital es San Sebastian'],
                        ['Beasaín‎','Éibar','Fuenterrabía‎','Hernani‎','San Sebastian']
                ],
                ['Vizcaya',
                    ['Su capital es Bilbao'],
                        ['Baracaldo','Bilbao','Erandio','Lejona‎']
                ]
            ]
        ],
        ['Principado de Asturias',
            [
                ['Asturias',
                    ['Su capital es Oviedo'],
                        ['Langreo','Mieres','Oviedo','Ponga']
                ]
            ]
        ],
        ['Región de Murcia',
            [
                ['Murcia',
                    ['Su capital es Murcia'],
                        ['Beniel','Bullas','Calasparra','Murcia']
                ]
            ]
        ]
    ]


print('Elige la CCAA que quieres para ver sus provincias. Pon el numero')
for i in range(len(arrayCCAA_Provincias)):
        print(str(i+1) + ' = '  + arrayCCAA_Provincias[i][0])

numero = introducirNumero('CCAA')
devolverProvincias_Ciudad_PorNumeroCCAA(numero,arrayCCAA_Provincias)
