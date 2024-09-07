'''
Nhập 1 số có 3 chữ số: 567
       hàng trăm, hàng chục, hàng đơn vị
input:     5      6           7

process: => tách số 3 chữ số thành từng số riêng lẻ
    B1: nhập số 3 chữ số
    B2: Lấy số hàng trăm
        hangTram = 567 //100 => 5
    B3: Lấy số hàng chục
        phanDu = 567 % 100 => 67
        hangChuc = 67 // 10 => 6
    B4: Lấy số hàng đơn vị
        hangDonVi = 67 % 10 => 7
    B5: cộng 3 số lại 
output:
 tổng các chữ số cộng lại
 5 + 6 + 7 => 18
'''
# B1
num = int(input("Nhập số có 3 chữ số: "))

# B2
hangTram = num //100
#B3
phanDu = num % 100 
hangChuc = phanDu // 10 

#B4
hangDonVi = phanDu % 10 

# B5
tong = hangTram + hangChuc + hangDonVi
print(f"Tổng của số 3 chữ số {num} là: {tong}")