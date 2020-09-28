def passw(password):
 
        validar=False #que se vayan cumpliendo los requisitos uno a uno.
        long=len(password) #Calcula la longitud de la contraseña
        espacio=False  #variable para identificar espacios
        mayuscula=False #variable para identificar letras mayúsculas
        minuscula=False #variable para contar identificar letras minúsculas
        numeros=False #variable para identificar números
        y=password.isalnum()#si es alfanumérica retorna True
        correcto=True #verifica que hayan mayúscula, minúscula, números y no alfanuméricos
        
        for carac in password: #ciclo for que recorre carácter por carácter en la contraseña
 
            if carac.isspace()==True: #Saber si el carácter es un espacio
                espacio=True #si encuentra un espacio se cambia el valor a True
 
            if carac.isupper()== True: #saber si hay mayúscula
                mayuscula=True #verificdor de mayúsculas
                
            if carac.islower()== True: #saber si hay minúsculas
                minuscula=True #verificador de minúsculas
                
            if carac.isdigit()== True: #saber si hay números
                numeros=True #verificador de números
        
                    
        if espacio==True: #hay espacios en blanco
            print("La contraseña no puede contener espacios")
        else:
            validar=True #se cumple el primer requisito que no hayan espacios
 
                       
        if long <8 and validar==True:
            print("Mínimo 8 caracteres")
            validar=False #Validar cambia a Flase si no se cumple el requisito mínimo de caracteres
 
 
        if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
           validar = True #Cumple el requisito de tener mayúscula, minúscula, números y no alfanuméricos
 
        else:
           correcto=False #uno o mas requisitos de mayúscula, minúscula, números y no alfanuméricos no se cumple
           
        if validar == True and correcto==False:
           print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")
 
        if validar == True and correcto ==True:
           return True