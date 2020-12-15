"""
โครงสร้างควบคุม  (Control Structur)
1. แบบลำดับ
2. แบบเลือก
3. แบบทำซ้ำ
"""

'''
if booexpression 
    statement 
'''
# การใช้ if จะเช็ค case ทุก case พร้อมกัน
# การใช้ elif จะเช็ค case ต่อ case


age =int(input("ป้อนอายุคุณ : "))
name="Aof attaporn"

if age>=15 and age<=20:
    print("วัยรุ่น")
    # ต้องมีการ Tap คำสั้่ง
    # pass คำสั่งผ่านไม่ต้องเช็ค
elif age>=21 and age<=31:
    print("วัยหนุ่มสาว")
elif age>=31 :
    print("วัยผู้ใหญ่")
else:
    print("วัยเด็ก")
print("จบโปรแกรม ")


# 15 - 20 => วัยรุ่น
# 21 - 30 => วัยหนุ่มสาว
# 31 - 40 => วัยผู็ใหญ๋

# and or not
# if condition :

"""
if จริง : 
    ทำอะไร 
else :  
    ทำอะไร
"""