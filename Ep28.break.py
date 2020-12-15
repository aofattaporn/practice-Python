# break     => ทำการเบลค
# continue  => ทำการกระโดดข้าม

print("========== break ================")
i=1
while i<=10:
    print("รอบที่ = ",i)
    if i==5:  # หากมีค่าเท่ากับ 5 จะทำการ break  และหลุดจาก loop
        break
    i+=1
else:
    print("จบโปรแกรม")

print("========== Continue ================")
j=1
while j<=10:
    j+=1 # 11
    if j==5:  # หากมีค่าเท่ากับ 5 จะทำการ ข้ามคำสั่ง print
        continue 
    print("รอบที่ = ",j) #11 
else:
    print("จบโปรแกรม")


