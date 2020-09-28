'''
Escribe un programa que pregunte una fecha en formato `dd/mm/aaaa` y muestre por pantalla la misma fecha 
en formato:
Investiga sobre el método split() para las cadenas de texto, te ayudará a separar los datos obtenidos
 a través de la fecha con formato `dd/mm/aaaa` , sino puedes usar el slicing que ya conoces.
`dd de <mes> de aaaa`
donde `<mes>` es el nombre del mes.
'''
diccionario_meses = {1:'Enero' ,2:'Febrero' ,3:'Marzo' ,4:'Abril' ,5:'Mayo' ,6:'Junio' ,7:'Julio' ,8:'Agosto' ,
9:'Septiembre' ,10:'Octubre' ,11:'Noviembre' ,12:'Diciembre'}

fecha = str(input('Introduce la fecha en formato dd/mm/aaaa = '))
#separamos los números de la fecha en una lista
lista_fecha = fecha.split("/")
mes_numero = int(lista_fecha[1]) # el mes es el segundo elemento
mes = str(diccionario_meses[mes_numero]) # lo sacamos del diccionario
print("Fecha ==> " , int(lista_fecha[0]) , " de " , mes , " de " , int(lista_fecha[2]) , " .")