# feeze bus 
# หาร 2 ลงตัวเป็น feeze 
# หาร 5 ลงตัวเป็น bus
# หาร 2 และ 5 ลงตัว เป็น feeze bus
"""
เช็คก่อนถึงค่อยปริ้น
"""
i=1
for i in range (1,100) : 
    if i%2==0 and i%5==0 : 
        print("feeze bus")
    elif i%2==0 : 
        print("feeze ")
    elif i%5==0 : 
        print("bus ")
    else:
        print(i)
