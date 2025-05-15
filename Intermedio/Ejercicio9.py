#9.
def lis_pairs(lista):
    pairs = []
    for i in lista:
        if i % 2 == 0:
            pairs.append(i)
    return pairs
lista = [1,2,12,4,5,7,6,9]
print(f"Los pares en la lista son: {lis_pairs(lista)}")