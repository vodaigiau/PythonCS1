n = int(input("nhap N:"))
sum = 0
soNguyen = 2

while soNguyen <= 2*n:
    sum += soNguyen
    soNguyen += 2
print(f"Tong S cac soNguyen {n} la:{sum}")