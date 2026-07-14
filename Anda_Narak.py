print("คำนวณกำไร")

quantity = int(input("จำนวนสินค้า : "))
cost_price = int(input("ต้นทุนต่อชิ้น : "))
sell_price = int(input("ราคาขายต่อชิ้น : "))

# คำนวณ
total_cost = quantity * cost_price
total_sell = quantity * sell_price
profit = total_sell - total_cost

print("----------------")
print("ต้นทุนทั้งหมด :", total_cost)
print("รายรับทั้งหมด :", total_sell)
print("กำไร :", profit)

# แบ่งให้บอส
boss_money = profit * 80 / 100
left = profit - boss_money

print("บอสได้อันดา :", boss_money)
print("เหลือ :", left)

# ลูกน้อง
team_members = int(input("จำนวนลูกน้อง : "))

team_money = left * 1 / 100
all_team = team_money * team_members

if all_team <= left:
    print("ลูกน้องรวมได้ :", all_team)
    print("ลูกน้องได้คนละ :", team_money)
else:
    print("เงินไม่พอแบ่งให้ลูกน้อง")

my_money = left - all_team


print("------------------")
print("สรุป")
print("------------------")

print("----------------")
print("กำไรสุทธิของเรา :", my_money)