# โปรแกรมคำนวณค่า BMI (ค่าดัชนีมวลกาน)
# BMI = น้ำหนัก(kg) / ส่วนสูง * ส่วนสูง (m)

weigth =int(input("กรุณษป้อนน้ำหนักของคุณ (kg) :"))
higth =int(input("ป้อนข้อมูลส่วนสูงข้องคุณ (cm) :"))
higth/=100
bmi = weigth/(higth*higth)
print("BMI = ",bmi)