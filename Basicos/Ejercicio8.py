#7
def count_letters():
    while True:
        word = input("ingrese una palabra: ")
        count = {}
        if word.isalpha():
            for i in word:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
            return count
        else:
            print("Ingresa solo letras. ")
            
print(count_letters())