# gọi x là lương mỗi giờ: (theo ví dụ của đề bài để tìm ra)
# => 40x + 1.5*5*x = 1425000 => x = 1425000/(49+1.5*5) => x = 30000

hourlyWages = 30000
salary = 0
hours = int(input("Vui long nhap so gio lam:"))

if hours < 40:
    salary = hourlyWages * hours
elif hours > 40:
    salary = hourlyWages * 40 + (hourlyWages * 1.5) * (hours - 40)

print("Luong cua ban la:", salary)
