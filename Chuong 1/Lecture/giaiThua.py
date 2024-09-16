n = int(input("Nhap so N:"))
giaiThua = 1
soNguyen = 1

while soNguyen <= n:
    giaiThua *= soNguyen
    soNguyen += 1

print(f"Giai thua cua {n} la: {giaiThua}")