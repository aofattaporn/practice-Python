list_a = []
list_b = []

a = [1, 5, 7]
b = [14, 10, 3]
sumList = a + b
sumList.sort()
increase = 1
print(sumList)
a = False

# ไม่เหมือนกันเลย False หมด
# มี True กรณีเดียวเป็น True
for item in sumList :
    if (item == sumList[increase]):
        a = a or True
        break
    else :
        a = a or False
        if(increase==len(sumList)-1):
            break
        increase += 1

print(a)

    # if(item == c[increase]) :
    #     print(True)
    # else:
    #     print()
    # increase += 1





