x = input("input :")
def backward(x) :
    if len(x) > 4 :
        x = (x[::-1])
    else :
        x = print(x)
    return x
print(backward(x))