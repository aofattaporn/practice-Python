import math
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))
m = b**2 - 4 * a * c
if m >= 0:
    if a != 0:
        x1 = (-b + math.sqrt(m)) / (2 * a)
        x2 = (-b - math.sqrt(m)) / (2 * a)
        print(x1)
        print(x2)
    else:
        x3 = -b/c
        print(x3)
else:
    print(" No Solution ")
