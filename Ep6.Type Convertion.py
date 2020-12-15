# Type Convertion การแปลงข้อมูล 
x =10
y =3.14
z ="20"

print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'str'>

# "20" => 20
# บวกเลข

result = x+int(z) # String => int
print(result)
result2 = str(x)+z
print(result2) # การ Concathination เก็บไว่ที่ result2