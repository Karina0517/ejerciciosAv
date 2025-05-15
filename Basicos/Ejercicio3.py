#3
def number_pair():
    while True:
        num = input("Ingresa un número entero: ")
        try:
            num = int(num)
            return num
        except:
            print("El número ingresado no es válido.")

number = number_pair()
if number % 2 == 0:
    print("Es par.")
else:
    print("Es impar.")