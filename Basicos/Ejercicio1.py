
#1
def personalized_greeting():
    
    while True:
        name = input("Escribe tu nombre: ")
        if name.isalpha():
            return (f"Hola, ¿Cómo estás? {name}")
        else:
            print("Nombre ingresado incorrecto. ")
            
print(personalized_greeting())

