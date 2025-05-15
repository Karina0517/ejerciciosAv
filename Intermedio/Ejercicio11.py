#11 factorial
def calculate_factorial():
    while True:
        number = input("INgrese un número para calcular su factorial. ")
        if number.isdigit():
            number = int(number)
            if number == 0 or number == 1:
                return 1
            else:
                fact = 1
                for i in range(2,number+1):
                    fact *= i
                return fact
        else: 
            print("Inresa un número válido")
            
print(calculate_factorial())