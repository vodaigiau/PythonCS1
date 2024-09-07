'''
    For 
    + ngắn gọn
    + thường xuyên dùng
    + Khó hiểu
'''

n = int(input("Nhập số n: "))
sum = 0

#?B1 & B2 & B4
#Khoảng giá trị từ 1 đến n: range(giá trị bắt đầu, giá trị kết thúc)
# Giá trị kết thúc = số n + 1 => range(1, 6) => 1,2,3,4,5
for so_nguyen in range(1, n + 1):
    #? B3
    print(so_nguyen)
    sum += so_nguyen
    
print(f"Tổng của số từ 1 cho đến {n} là: {sum}")