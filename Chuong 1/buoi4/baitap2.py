'''
test case
n = 4 => 2*n => 8
S = 2 + 4 + 6 + 8

n = 5 => 2*n => 10
S = 2 + 4 + 6 + 8 + 10

n = 6 => 2*n => 12
S = 2 + 4 + 6 + 8 + 10 + 12 

Kết luận:
- giữa các số hạng chênh lệch 2 đơn vị => giúp xác định giá trị cần tăng
- Dừng cộng khi cộng vào 2*n => đk dừng hoặc tiếp tục loop

IPO
input: n (ví dụ 4)
        2n : 8
process:
    B1: cho người dùng nhập n
    B2: Tạo biến có giá trị thay đổi (so_hang)
    B3: điều kiện lặp
        so_hang <= 2*n
    B4: Code cần thực hiện lặp lại
         - cộng số hạng vào tổng
    B5: tăng giá trị của so_hang (tăng 2)
    B6: thông báo kết quả
    
output:
    sum (20)

'''


#? B1
n = int(input("Nhập số n: "))
#? B2
so_hang = 2
sum = 0

#? B3
while so_hang <= 2*n:
    #? B4
    # sum = sum + so_hang
    sum += so_hang
    #? B5
    # so_hang = so_hang + 2 
    so_hang += 2
    
#? B6
print(f'Tổng S của 2*{n}: {sum} ')