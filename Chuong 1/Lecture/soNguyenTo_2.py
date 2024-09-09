
import math

n = int(input("Nhap n:"))
soChia = 2
count = 0
ketLuan = True
while(soChia <= math.sqrt(n)):
    count +=1
    if(n % soChia == 0):
        ketLuan = False
        break
    soChia += 1

print(count)
if(ketLuan and n > 1):
    print(f"{n} la so nguyen to")
else:
    print(f"{n} khong phai la so nguyen to")
    