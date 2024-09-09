n = int(input("Nhap n:"))
sum = 0
soNguyen = 1

while soNguyen <= n:
    sum += soNguyen
    soNguyen += 1
print(f"Tong cac so nguyen {n} la: {sum}")