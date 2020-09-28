#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
class Perros(object): #La clase principal Perros
    def __init__(self, nombre, peso): #Define los parámetros
        self.__nombre = nombre #Declara los atributos (privados ocultos)
        self.__peso = peso
    @property
    def nombre(self): #El método para obtener el nombre(sería el getter)
        "Documentación del método nombre bla bla" # Doc del método
        return self.__nombre #Aquí simplemente retorna el atributo privado oculto
 
 
#Hasta aquí los métodos para obtener los atributos ocultos o privados getter.
#Ahora utiliza setter y deleter para modificarlos
 
    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print ("El nombre se ha modificado por")
        print (self.__nombre) #Aquí se vuelve a pedir que retorne el atributo para confirmar
    @nombre.deleter #Propiedad DELETER
    def nombre(self):
        print("Borrando nombre..")
        del self.__nombre
        
        #Hasta aquí property#
 
    def peso(self):    #Método para obtener el peso
        return self.__peso #Aquí simplemente retorna el atributo privado
 
#Instanciamos
Mira = Perros('Mira', 13)
print (Mira.nombre) #Imprime el nombre de Mira. Se hace a través de getter
#Que en este caso como está después de property lo toma como el primer método.
 
Mira.nombre = 'Pingüino' #Cambiamos el atributo nombre que se hace a través de setter
del Mira.nombre #Borramos el nombre utilizando deleter