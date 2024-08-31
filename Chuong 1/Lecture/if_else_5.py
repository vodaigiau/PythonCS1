a = int(input("Nhap so thu 1:"))
b = int(input("Nhap so thu 2:"))
c = int(input("Nhap so thu 3:"))

if a <= b and b <= c:
    print(f"Thứ tự tăng dần: {a}, {b}, {c}")
elif a <= c and c <= b:
    print(f"Thứ tự tăng dần: {a}, {c}, {b}")
elif b <= a and a <= c:
    print(f"Thứ tự tăng dần: {b}, {a}, {c}")
elif b <= c and c <= a:
    print(f"Thứ tự tăng dần: {b}, {c}, {a}")
elif c <= a and a <= b:
    print(f"Thứ tự tăng dần: {c}, {a}, {b}")
else:
    print(f"Thứ tự tăng dần: {c}, {b}, {a}")
    
