# ตัวดำเนินการทางตรรกศาสตรื
# ดปรียบเทียบค่า 2 ฝั่ง
# 2 คำตอบ =>  True or False
"""
AND = และ ตัวใดตัวนึงเป็น false จะเป็น false ทั้งหมด
OR = หรือ ตัวใดตัวนึงเป็น True จะเป็น True ทั้งหมด
NOT = ไม่ ตรงข้าม
"""
x =(5>10) # ค่า x = bool => false
y =(10==5) # ค่าy = bool => false
print(x)
print(y)

# z = (5>10) and (10==5)
z = x and y
print("ค่า x and y = ", z)
                              
m=(10!=5) or (10==5) # => True
print("ค่าของ (10!=5) or (10==5) = ",m)