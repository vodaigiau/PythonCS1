num = int(input("Nhap so co 3 chu so:"))

hangTram = num // 100
phanDu = num % 100
hangChuc = phanDu // 10
hangDonvi = phanDu % 10

sum = hangTram + hangChuc + hangDonvi
print(f"Tong 3 so cua {num} la: {sum}")