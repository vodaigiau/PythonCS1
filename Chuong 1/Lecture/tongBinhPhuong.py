n = int(input("Nhap N:"))
tongBinhPhuong = 0
soNguyen = 1

while soNguyen <= n:
    tongBinhPhuong += soNguyen * soNguyen
    soNguyen += 1

print(f"Tong cac so nguyen bang binh phuong cua {n} la: {tongBinhPhuong}")