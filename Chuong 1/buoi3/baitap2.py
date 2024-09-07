'''
input:
    khối lượng (weight/ kg)
    khoảng cách (distance/ km)
Process:
    B1: Yêu cầu nhập inputs
    B2: Kiểm tra kg
        Nếu kg < 3, 20000/kg
        Ngược lại, 30000/kg
    B3: Kiểm tra km
        Nếu kg < 10, 20000/km
        Ngược lại, 30000/km
    B4:
        tổng ship = chi phí km + chi phí kg
    
Output:
    tổng tiền ship (total)

'''
# B1:
kg = float(input("Nhập khối lượng: "))
km = float(input("Nhập khoảng cách: "))

#B2:
if kg < 3:
    #True
    price_kg = kg * 20000
else:
    #False
    price_kg = kg * 30000
    
#B3
if km < 10:
    #True
    price_km = km * 20000
else:
    #False
    price_km = km * 30000
    
#B4
total = price_kg + price_km

print("Tổng tiền ship là: ", total)