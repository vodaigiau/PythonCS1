'''
so_chia = 2

so_chia <= căn bậc 2 của n

5/2,                   5/3, 5/4, 5/5
2,2
chia hết: 0

6/2,           6/3,6/4, 6/5, 6/6
2,449
chia hết: 1

7/2,       7/3,7/4, 7/5, 7/6, 7/7
2,646
chia hết:0

8/2,        8/3,8/4 , 8/5, 8/6, 8/7, 8/8
2,828
chia hết 1

10/2, 10/3,             10/4, 10/5,10/6, 10/7, 10/8, 10/9, 10/10
3,162
chia hết 1

11/2, 11/3,                 11/4, 11/5,11/6, 11/7, 11/8, 11/9, 11/10, 11/10
3,316
chia hết 0

16/2,       16/3, 16/4
4
chia hết 2 => chỉ cần xét có 1 số chia hết lặp tức dừng vòng không cần xét thêm nữa

'''
#cài đặt thư viện hỗ trợ toán học
import math 

#? B1:
n = int(input("Nhập số n: "))
#? B2: xác định giá trị biến cần đổi
so_chia = 2
count = 0
#Cờ hiệu
ket_luan = True #giả sử là số nguyên tố

#? B3:điều kiện lặp
while so_chia <= math.sqrt(n):
    #? B4: code cần lặp
    count +=1 
    if n % so_chia == 0: #kiểm chứng 
        # chia hết
        ket_luan=False #cập nhật giá trị cờ hiệu
        break #bắt dừng vòng lặp cho dù vẫn thỏa điều kiện
    #? B5: tăng giá trị của biến so_chia
    so_chia +=1
   
    
print(count)  
# ket_luan == True => rút gọn thành ket_luan
if ket_luan and n > 1:
    print(f"Số {n} là số nguyên tố")
else:
    print(f"Số {n} là không phải số nguyên tố")