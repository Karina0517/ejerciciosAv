#EJERCICIOS BÁSICOS:

# 1.
def personalized_greeting(name):
    return (f"Hola, ¿Cómo estás? {name}")

name = input("Escribe tu nombre: ")
print (personalized_greeting(name))

#2.
def addition_numbers(n1,n2):
    sum = (n1 + n2)
    return sum
n1 = int(input("Escribe el primer número a sumar: "))
n2 = int(input("Escribe el segundo numero a sumar: "))
print (addition_numbers(n1,n2))

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
 
#4   
def age_adult(age):
    if age >= 18:
        print ("Es mayor de edad. ")
    else:
        print ("Es menor de edad. ")
age = int(input("Ingrese una edad: "))
age_adult(age)

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

#6
def triangle_area():
    base = int(input("Ingrese la base del triangulo: "))
    altura = int(input("Ingrese la altura del triangulo: "))
    area = (base*altura)/2
    return area
print (triangle_area())

#7
def count_letters():
    word = ("karina")
    count = {}
    for i in word:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(count_letters())

#NIVEL INTERMEDIO
#9.
def lis_pairs(lista):
    pairs = []
    for i in lista:
        if i % 2 == 0:
            pairs.append(i)
    return pairs
lista = [1,2,12,4,5,7,6,9]
print(lis_pairs(lista))

def palindromo(word):
    rWord = word[::-1]
    if word == rWord:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
        
palindromo("ana")
import random
def validate_password(password):

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
        return True
    else:
        return False

validate_password("Kari2772019*")

#17
def dade_r():
    return random.randint(1, 6)
dade_r()

#18
def add_uniques(lst):
    total = 0
    for num in lst:
        if lst.count(num) == 1:
            total += num
    return total
lis = [1,2,3,4,5,1,2]
add_uniques(lis)

#19
import random

def generate_password(longitud):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    simbol = "!@#$%^&*()"
    
    todos = letters + numbers + simbol
    password = ""
    
    for i in range(longitud):
        caracter = random.choice(todos)
        password += caracter
    
    return password

print (generate_password(8))

#20
def add_2(x):
    return x + 2

def multiply_3(x):
    return x * 3

def comp_function(valor):
    add = add_2(valor)
    result = multiply_3(add)
    return result
print(comp_function(5))


    
    
