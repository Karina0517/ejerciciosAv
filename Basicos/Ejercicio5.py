#5
def temp():
    while True:
        temp = input("Ingresa un la temperatura en Celcius: ")

        try:
            temp = float(temp)
            return temp
        except:
            print("Ingresaste un dato no válido.")

temp_C = temp()
temp_F = (temp_C * (9 / 5) + 32)

print("La temperatura en Fahrenheit es: " + str(temp_F))