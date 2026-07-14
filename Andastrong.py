name = str(input("ขื่ออะไร : "))
age = int(input("อายุ : "))
tall = int(input("สูงเท่าไหร่ : "))
Strong = int(input("ความแข็งแกร่ง : "))
money = int(input("เงินติดตัว :"))
Stat = tall+Strong+money

if tall >= 170:
    print("ผ่านที่170 คุณคือ" , tall ,"คุณผ่าน")
else:
    print("ไม่ผ่านไปไกลๆ")

if Strong > 100:
    print("ผ่านที่100 คุณได้ :" , Strong ,"คุณผ่าน")
else:
    print("ไม่ผ่าน")

if money > 30:
    print("ผ่านที่20 :" , money , "คุณผ่าน")
else:
    print("ไปไกลๆไอจน")

if Stat > 300:
    print("ขี้ค่า")
elif Stat > 350:
    print("ลูกน้องนิดนึง")
elif Stat > 400:
    print("บอดี้การ์ด")
elif Stat > 450:
    print("มือขวา")
else:
    print("ไปตายไป")