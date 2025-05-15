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