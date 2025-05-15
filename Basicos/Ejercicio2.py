#2.
def addition_numbers():
    while True:
        n1 = input("Escribe el primer número a sumar: ")
        n2 = input("Escribe el segundo numero a sumar: ")
        if n1.isdigit() and n2.isdigit():
            sum = (int(n1) + int(n2))
            return sum
        else:
            print("Numero ingresado incorrecto")

print (addition_numbers())