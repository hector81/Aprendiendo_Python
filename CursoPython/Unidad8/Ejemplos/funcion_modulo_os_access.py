'''
Saber si se puede acceder a un archivo o directorio.  

>>>os.access(path, modo_de_acceso)
'''
  
import os
path1 = os.access("/Users/user/Desktop/IV Curso AERTIC-UR. Tendencias en IT Iniciación a La Programación en Python 3/CursoPython", os.F_OK) 
print("Exists the path:", path1) 
  
# Checking access with os.R_OK 
path2 = os.access("/Users/user/Desktop/IV Curso AERTIC-UR. Tendencias en IT Iniciación a La Programación en Python 3/CursoPython", os.R_OK) 
print("Access to read the file:", path2) 
  
# Checking access with os.W_OK 
path3 = os.access("/Users/user/Desktop/IV Curso AERTIC-UR. Tendencias en IT Iniciación a La Programación en Python 3/CursoPython", os.W_OK) 
print("Access to write the file:", path3) 
  
# Checking access with os.X_OK 
path4 = os.access("/Users/user/Desktop/IV Curso AERTIC-UR. Tendencias en IT Iniciación a La Programación en Python 3/CursoPython", os.X_OK) 
print("Check if path can be executed:", path4)