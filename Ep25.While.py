# โครงสร้างควบคุมแบบทำซ้ำ 
"""
while expression : 
        statement
"""
i =1 # จำนวนของรอบ 
sum=0
x = int(input("กรุณาป้อนจำนวน : "))
while i<=x : 
    sum+=i
    print("มีทั้งหมด ",i," จำนวน"," ได้ผลบวกคือ ",sum)
    i+=1
avg =sum/x
print("เพราะฉะนั้นจะมีค่าเฉลี่ยยเท่ากับ ", avg)


