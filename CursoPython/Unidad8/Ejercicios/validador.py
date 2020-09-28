import usuario
import contrasena
 
correcto=False
while correcto==False:
        nombre=input("Ingrese nombre de usuario: ")
        if usuario.usuario(nombre) == True:
            print("Usuario creado exitosamente")
            correcto=True
 
while correcto==True:
    contrasenia=input("Ingrese su Password: ")
    if contrasena.passw(contrasenia)==True:
        print("Contraseña creada exitosamente")
        correcto=False