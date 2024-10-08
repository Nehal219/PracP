from itertools import accumulate

l = [1,2,3,4,5,6]

def fun(a,b):
    return a*b

res = accumulate(l,fun)
print(list(res))