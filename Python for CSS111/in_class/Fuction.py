"""
การสร้าง function เพื่อให้โปรแกรมเป็นระเบียบขึ้น
def functname(x1, x2, x3, x4): เวลาจะใช้ fuction นี้จะต้องส่ง parameter 4 ตัว
    X = X1 + x2 + x3 + x4
    ( statement ) --> สามารถใช้งานพารามิเตอร์ในนี้ได้
    return x      --> เอาไปใช้งานต่อได้
"""

def read_data() :
    n = int(input())
    d = [0]*n
    for i in range(n):
        d[i] = int(input())
    return d

# recursive function การเรียกฟังชั่นตัวเอง
def fact(n):
    f = n * fact(n-1)
    return f

# ตัวแปรที่อยู่ใน function ว่า local variable
# def mean(d)  : --> type error มีการตั้งชื่อซ้ำกัน function กับ list
#     return sum(d) / len(d)
# mean = mean([3, 3, 4, 6, 4])
# mean = mean([34, 4, 35, 6])

# สามารถสร้าง พารามิเตอร์สองตัวได้ แต่จะมีการแทนที่
def average(a, b):
    return (a+b)/2
def average(a, b, c): # ใช้ พารามิเตอร์อันนี้
    return (a+b+c)/2
print( average(1,2,3))
print(average(4,5,4))

# default argrument values
def raises(x, n=2) :
    return pow(x, n)

# lambda function
x = lambda a : a + 10
print(x(5))

# scope of varaible --> สามารถมีตัวแปรใน ตัว function และ main program ได้
# ไม่เหมือนกับ  list