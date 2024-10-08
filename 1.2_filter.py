ages = [23,64,3,44,25,16,17,15,19]

def fun(age):
    if age >= 18:
        return True
    elif age < 18:
        return False

result = filter(fun,ages)
print(list(result))