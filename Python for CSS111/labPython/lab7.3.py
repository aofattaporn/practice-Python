row = 4
column = 10
PV = 1
i = 1  # แถว
j = 1 # หลัก
k = 1

x = 1 * ((1+ (4/100) )** 1)
print(x)
print("period  ", end=" ")

for j in range(j, column+1):         # วนหาหลักตัวเลขก่อน
    print("%3d"%(j),"%" ,'\t', end=" ")
    j +=1
j = 1                               # reset j ( reset แถว )

for i in range(i, row+1):           # วนหาตามแถวของตัวเลข
    print('\n', i, '\t\t', end="   ") # ปริ้นเลขcolum และtape ใช้ตัวแปร i

    for k in range(column) :         # ตัวแปรในการกำหนดรอบ loop เล็กโดยตัวแปร k (ในตาราง)
        FV = PV * ((1 + (j / 100)) ** i) # สมการการคิดเลขความสัมพันธ์ colum and row
        print('%5.3f'%(FV), end="   ")
        k +=1                       # เพิ่มค่า k
        j +=1                       # เพิ่มค่า j

    j = 1                           # reset ตัวแปร j
    i +=1                           # เพิ่มตัวแปร i
