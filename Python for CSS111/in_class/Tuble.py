"""
คล้ายกับ List แต่เปลี่ยนแปลงไม่ได้
ใช้ วงเล็บ ()
 Edit แก้ไขเปลี่ยนแปลงไม่ได้
 ปกติจะใช้สำหรับค่าที่ไม่มีการเปลี่ยนแปลง ex day_of_week  
"""
# >>> book = ("data", "2143434", 28.999)
# >>> book[0] = "Infomation"
primes = [2, 3, 4, 5, 6, 7]
price = (256.75,)
price2 = (10,)
price3 = price2 + price
print(price3)