import random

def generate_password():
    longitud= int(input("Ingrese la longitud de la contraseña a crear: "))
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    simbol = "!@#$%^&*()"
    
    todos = letters + numbers + simbol
    password = ""
    
    for i in range(longitud):
        caracter = random.choice(todos)
        password += caracter
    
    return password

print (generate_password())