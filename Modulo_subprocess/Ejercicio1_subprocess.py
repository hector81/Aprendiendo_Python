'''
EJERCICIOS MÓDULO subprocess 1. Cree un script que realice una llamada al
comando ipconfig (en windows, ifconfig en linux). Recupere las direcciones
IPv4 e IPv6 de su equipo a partir de la salida de dicho comando
'''
import subprocess

configuracionIPV4_IPV6_Windows = subprocess.call(["ipconfig"], stdin=None)
archivo_texto_salida = subprocess.check_output("ipconfig")

ListaPuertosTCP = subprocess.call(["netstat" , "-a"], stdin=None)
