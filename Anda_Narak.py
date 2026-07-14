print("คำนวณกำไรค้าอาวุธเถื่อน")
#จำนวณ
quantity = int(input("จำนวนปืนที่รับมาขาย : "))
cost_price = int(input("ต้นทุนของปืนที่รับมาต่อละกระบอก : "))

#ราคาต้นทุนของปืนทั้งหมด
total_cost = cost_price * quantity
print("กำไร" , total_cost)

#จะขายปืนเท่าไหร่
sell_price= int(input("ราคาที่จะนำไปขายต่อ : "))
Gumrai = sell_price*quantity
print("ถ้าขายหมดในราคานี้จะได้เงินทั้งหมด" , Gumrai )

#Boss_Anda = 80%
Boss_Anda = Gumrai *80 /100 
print("บอสอันดาถือหุ้น80% แปลวาบอยจะได้เงินไป : " , Boss_Anda)

#เหลือ
Left = Gumrai - Boss_Anda 
print("จะเหลือเงิน", Left)
#team_members = 1% ต่อคน
#ขี้ค่า
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน :"))
team_money = Left *1 /100
moneyReally = team_members*team_money
if moneyReally > Left:
    print("ไม่ต้องเอา")
else:
    print("ลูกน้องจะได้เงิน" ,moneyReally)


print("สรุป")
print("------------------")

print("เงินกำไรของเราเหลือทั้งหมด กำไรสุทธิ :" , Left - moneyReally)
print("ต้นทุน :" , total_cost)
print("รายรับทั้งหมด: " ,Gumrai)
print("จำนวนที่ให้บอสอันดา", Boss_Anda)
print("จำนวนเงินที่ลูกน้องได้ต่อคน", team_money)