n = int(input("Nhap n:"))
soChia = 1
soLuongUoc = 0
count = 0
while(soChia <= n/2):
    if(n % soChia == 0):
        soLuongUoc += 1
    soChia += 1
    count +=1
if(soLuongUoc == 1 and n > 1):
    print(f"{n} la so nguyen to")
else:
    print(f"{n} khong phai la so nguyen to")
    