x = float(input("เงินได้สุทธิ : "))

if x >= 150001 and x <= 300000:
    m1 = (x - 150000) * 0.05
    print(m1, " บาท")
elif x >= 300001 and x <= 500000:
    m2 = (x - 300000) * 0.1 + 7500
    print(m2, " บาท")
elif x >= 500001 and x <= 750000:
    m3 = (x - 500000) * 0.15 + 27500
    print(m3, " บาท")
elif x >= 750001 and x <=1000000:
    m4 = (x - 750000) * 0.20 + 65000
    print(m4, " บาท")
elif x >= 1000001 and x <= 2000000:
    m5 = (x - 1000000) * 0.25 + 115000
    print(m5, " บาท")
elif x >= 2000001 and x <= 5000000:
    m6 = (x - 2000000) * 0.30 + 365000
    print(m6, " บาท")
elif x >= 5000001:
    m7 = (x - 5000000) * 0.35 + 1265000
    print(m7, " บาท")
else:
    print("Hurry, tax exampleed" )




