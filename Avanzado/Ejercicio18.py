#18
def add_uniques(lst):
    total = 0
    for num in lst:
        if lst.count(num) == 1:
            total += num
    return total
lis = [1,2,3,4,5,1,2]
add_uniques(lis)
