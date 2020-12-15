# มีจำนวนรอบที่ชัดเจน มีจุดเริ่มต้น 
# for in range(stat,stop,step) # กำหนดรอบ 
for i in range(1,6,2): # index=0 เพิ่มค่าขึ้นท่ีละ 2 
    print("รอบที่ = ",i,"Hello world")

# การทำ summation 
summation =0
for i in range(6):  # suumation 
    summation+=i
    print("รอบที่ =",i," sum = ",summation)
print("ผลรวม =",summation)
print("ผลรวม =",summation/6)