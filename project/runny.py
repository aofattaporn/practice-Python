#โปรแกรมคำนวณค่าดัชนีมวลกาย(bmi)
#หากไม่กรอกจำนวน
print("========== โปรแกรมคำนวณค่า BMI ==============")
i=int(input("หากต้องการทำงานกดหมายเลข 1 :"))
sum_fmbmi=0 # ผลรวมตั้งต้น bmi ของผู้หญิง
sum_mbmi=0 # ผลรวมตั้งต้น bmi ของผู้ชาย 
m=1   # จำนวนตั้งต้นของผู้ชาย
fm=1  # จำนวนตั้งต้นของผู้หญิง
x=1

while i==1  : 
    x=int(input("หากเพศชายกด 1 หากเพศหญิงกด 2 : "))

    if x==1 :
        mw = float(input("Enter weight (kg): "))
        mh = float(input("Enter high (cm): "))/100
        mbmi = mw/(mh**2) 
        sum_mbmi+=mbmi # ผลรวม bmi ของชาย
        m +=1 # จำนวนของหญิง
        if mbmi<18.0:
            result="น้ำหนักต่ำกว่าเกณฑ์/ผอม"
        elif mbmi>=18.5 and mbmi<=22.9:
            result="สมส่วน"
        elif mbmi>=23.0 and mbmi<=24.9:
            result="เริ่มท้วม"
        elif mbmi>=25.0 and mbmi<=29.9:
            result="อ้วน"
        elif mbmi>=30:
            result="อ้วนมาก"
        else :
            result="ไม่ทราบค่า"
        print("ค่า bmi = ", mbmi ,"คาดคะเนว่า = ", result)
        print("---------------------------------------")
    elif x==2 : 
        fmw = float(input("Enter weight (kg): "))
        fmh = float(input("Enter high (cm): "))/100
        fmbmi = fmw/(fmh**2) 
        sum_fmbmi+=fmbmi # ผลรวม bmi ของผู้หญิง
        fm +=1 # จำนวนของหญิง
        if fmbmi<18.0:
            result="น้ำหนักต่ำกว่าเกณฑ์/ผอม"
        elif fmbmi>=18.5 and fmbmi<=22.9:
            result="สมส่วน"
        elif fmbmi>=23.0 and fmbmi<=24.9:
            result="เริ่มท้วม"
        elif fmbmi>=25.0 and fmbmi<=29.9:
            result="อ้วน"
        elif fmbmi>=30:
            result="อ้วนมาก"
        else :
            result="ไม่ทราบค่า"
        print("ค่า bmi = ", fmbmi ,"คาดคะเนว่า = ", result)
        print("---------------------------------------")
    i=int(input("หากต้องการทำงานต่อกด 1 :")) 
if m!=1 :
        m=m-1
elif fm!=1 :
        fm=fm-1
print("====> ค่าเฉลี่ยของผู้ชาย ",sum_mbmi/m) 
print("====> ค่าเฉลี่ยของผู้หญิง ",sum_fmbmi/fm)
print("====> ค่าเฉลี่ยรวม ",(sum_fmbmi+sum_fmbmi)/(m+fm))
print("========== สิ้นสุดการทำงาน ====================")