'''
Tính tổng các số từ 1 đến n
tong = 1 + 2+ 3 + 4+ 5
tong = + 1 (so_nguyen)
tong = + 2
tong = +3
while
+ thường dùng
+ Dễ hiểu

'''

# Giả sử n= 5 => 1,2,3,4,5 => dãy số nguyên dương
n = int(input("Nhập số n: "))
sum = 0 #quy định biến sum là kiểu số
#? B1: xác định giá trị quy đinh điều kiện lặp
so_nguyen = 1
#? B2: kiểm tra điều kiện lặp => while biểu thức so sánh
while so_nguyen <= n:
    #? B3: Các đoạn code cần lặp lại
        print(so_nguyen)
        # sum = sum + so_nguyen
        sum += so_nguyen
    #? B4: Thay đổi giá trị của biến so_nguyen
        # 1 + 1 => 2 + 1=>  3
        # đọc phải trước, trái sau => so_nguyen ban đầu là 1 + 1 => gán giá trị 2 vào lại biến so_nguyen
        #so_nguyen (sau tăng) = so_nguyen (giá trị trước tăng) + 1 # biến tích lũy
        so_nguyen +=1
 
print(f"Tổng của số từ 1 cho đến {n} là: {sum}")   