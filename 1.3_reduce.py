from functools import reduce

l = [1,2,3,4,5,6]

def sum(a,b):
    return a*b

res = reduce(sum,l)
print(res)