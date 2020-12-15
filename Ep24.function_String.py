name = " kong " # index => 0 
name2 = "ไปซื้อข้าวและอาหารที่ตลาด"
#print("อายุเท่าไหร่ = ",name[-2:]) #ก่อนถึงจุดสิ้นสุดท้าย

print(len(name))
name=name.strip() # ลบช่องว่างซ้ายขวา (strip)
print("ช่องว่างระหว่างข้อความ fuction(len) =>",len(name))

print("แปลง ให้เป็นตัวพิมพ์เล็กทั้งหมด =>" ,name.lower())   # แปลง ให้เป็นตัวพิมพ์เล็กทั้งหมด
print("แปลง ให้เป็นตัวพิมพ์ใหญ่ทั้งหมด =>" ,name.upper())  # แปลง ให้เป็นตัวพิมพ์ใหญ่ทั้งหมด
print("แปลง ตัวหน้าให้เป็นตัวพิมพ์ใหญ่ =>" ,name.capitalize()) # แปลง ตัวหน้าให้เป็นตัวพิมพ์ใหญ่
print("แปลง การแทนที่  =>" ,name.replace("kong","555")) # การแทนที่ 
x = "ข้าว" in name2
print(x)
if x : 
   name2=name2.replace("ข้าว","ไข่")
print("แปลง คำหนึ่งเป็นอีกคำ =>",name2)

fname = "Aof"
lname = "ruksiam"
age = "60"
salary = 500.231
fullname = fname+lname+age  # การต่อ String (Concatinate) "+"
print("การทำ Concatinate =>","ชื่อต้น :"+fname+"นามสกุล :"+lname+"\tอายุ :"+age)
test = "การทำ format      => ชื่อต้น :{2} นามสกุล :{1} อายุ :{2} อาชีพ:{3} เงินเดือน:{4:.2f}"
print(test.format(fname,lname,age,"โปรแกรมเมอร์",salary)) # การทำ format String

fruit="ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด"
print("นับจำนวนคำว่าทุเรียน มี ",fruit.count("ทุเรียน"),"คำ") # นับจำนวนคำในประโยค (count)
print("เช็คคำขึ้นต้น  =>",name.startswith("นาย")) #เช็คคำขึ้นต้น
print("เช็คคำลงท้าย =>",name.endswith("นาย"))  #เช็คคำลงท้าย
