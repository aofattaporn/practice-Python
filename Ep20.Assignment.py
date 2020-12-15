# แลกเงินและหาจำนวนแบงค์
# 2000 => 1000 ==> 2 ใบ
# 1500 ==> 1 ใบ ม 500 = 1 ใบ
number = int(input("ป้อนจำนวนเงินของคุณ : "))

if number >= 1000 :
    print ("มีแบงค์ 1000 บาทจำนวน ",number//1000, "ใบ")
    number=number%1000
if number>= 500:
    print("มีแบงค๋ 500 บาทจำนวน ",(number//500), "ใบ")
    number = number % 500
if number>= 100:
    print("มีแบงค๋ 100 บาทจำนวน ",(number//100), "ใบ")
    number = number % 100
if number>= 50:
    print("มีแบงค๋ 50 บาทจำนวน ",(number//50), "ใบ")
    number = number % 50
if number>= 20:
    print("มีแบงค๋ 20 บาทจำนวน ",(number//20), "ใบ")
    number = number % 20

if number>= 10:
    print("เหรียญ 10 บาทจำนวน ",(number//10), "เหรียญ")
    number = number % 10
if number>= 5:
    print("เหรียญ 5 บาทจำนวน ",(number//5), "เหรียญ")
    number = number % 5
if number>= 1:
    print("เหรียญ 1 บาทจำนวน ",(number//1), "เหรียญ")
    number = number % 1

