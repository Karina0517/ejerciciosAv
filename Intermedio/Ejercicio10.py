def palindromo():
    while True:
        word = input("Ingrese una palabra para saber si es palíndromo: ")
        if word.isalpha():
            rWord = word[::-1]
            if word == rWord:
                return("Es un palíndromo")
            else:
                print("No es un palíndromo")
        else:
            print("Debes ingresar un número. ")
        
print(palindromo())