x = [2, 1, 3]
my_sum = 0

# การใช้ fuction จาก List
print(x)
print("การหาค่าจำนวนสูงสุง :", max(x))                  # การหาตัวที่มากสุดใน list
print("การหาค่าจำนวนต่ำสุด :", min(x))                  # การหาตัวที่น้อยสุดใน list
print("จำนวนสมาชิกภานใน list :", len(x))              # การนับจำนวนภานใน list
print("การหาผลรวมใน list :", sum(x))                 # การหาผลรวมของ list
print("การหาจำนวนของตัวเลขใน list :", x.count(2))     # การหาจำนวนตัวภานใน list

# การใช้ .sort --> การเรียงลำดับจากน้อยไปมาก
a = x.sort() # ทำการเรียงค่าแต่ไม่มีการคืนค่า
print(a)                                     # ไม่มีหารคืนค่าในการ sort = none
print("การเรียงตัวเลขจากน้อยไปมาก x =", x)      # มีการเรียงภายใน x.sort
a = x.sort(reverse=True)                     # การคืนค่ากลับกลายเป็น จากน้อยไปหามาก
print("การเรียงตัวเลขจากมากไปน้อย x =", x)
for i in x : # มีการเข้าถึง ทุกตัวใน list x
    my_sum = my_sum + i
print("ผลรวมมากสุด", my_sum)
print("ผลรวมมากสุด", sum(x))

# index slicing
x.sort()
print(x)
print("index0 - 9(สุดท้าย)", x[:10]) # ing
print("idx0 - idxo", x[:1])  # ind0 - ind0
print("idx0 - idx2", x[:-3]) # index ี่ 3 จากขวา
print("idx1 - idxสุดท้าย",x[2:]) # index3 - indexสุดท้าย

# การลบข้อมูล ใน list
w = [0, 1, 2, 3]
w.pop(3) # การลบ index ที่ 3
print(w)

# String method


inline = input("Birthdate (dd/mm/yyyy) :")
[d, m, y] = inline.split("/")
