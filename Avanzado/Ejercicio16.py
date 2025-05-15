def validate_password():
    password = input("Ingresa una contraseña que contenga al menos una letra mayúcula, una minúscula, un número y un caracter especial. ")
    for caracter in password:
        if caracter == caracter.upper() and caracter.isalpha():
            mayus = True
        elif caracter == caracter.lower() and caracter.isalpha():
            minus = True
        elif caracter.isdigit():
            num = True
        elif caracter in "!@#$%^&*()_+-=[]{}|;:',.<>?/":
            simbol = True

    if mayus and minus and num and simbol:
        return ("Contrasena correcta. ")
    else:
        print ("Contraseña incorrecta, ingresa una nueva. ")

print(validate_password())