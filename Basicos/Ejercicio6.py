#6
def triangle_area():
    while True:
        base = input("Ingrese la base del triangulo: ")
        altura = input("Ingrese la altura del triangulo: ")
        try:
            base = float(base)
            altura = float(altura)
            area = (base*altura)/2
            return area
        except:
            print("Ingresaste un número no válido. ")
print (triangle_area())