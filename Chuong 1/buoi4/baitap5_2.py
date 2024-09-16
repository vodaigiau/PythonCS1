# Tối ưu chương trình
# tốc độ xử lý của chương trình (time)
# lần lặp nhiều => chậm ; lặp ít => nhanh

'''
ctr + d: tìm các nội dung giống, tạo đa con trỏ

so_chia <= n/2

5/1, 5/2,                   5/3, 5/4, 5/5
ước 1

6/1, 6/2, 6/3,              6/4, 6/5, 6/6
ước: 3

7/1, 7/2, 7/3,              7/4, 7/5, 7/6, 7/7
ước: 1

8/1, 8/2, 8/3,8/4           , 8/5, 8/6, 8/7, 8/8
ước: 3

10/1, 10/2, 10/3, 10/4, 10/5,               10/6, 10/7, 10/8, 10/9, 10/10
ước: 3

11/1, 11/2, 11/3, 11/4, 11/5,         11/6, 11/7, 11/8, 11/9, 11/10, 11/10
ước: 1
'''


#? B1:
n = int(input("Nhập số n: "))
#? B2: xác định giá trị biến cần đổi
so_chia = 1
so_luong_uoc = 0
count = 0

#? B3:điều kiện lặp
while so_chia <= n/2:
    #? B4: code cần lặp
    if n % so_chia == 0:
        # chia hết
        so_luong_uoc +=1
    #? B5: tăng giá trị của biến so_chia
    so_chia +=1
    count +=1 
    
print(count)  

if so_luong_uoc == 1 and n > 1:
    print(so_luong_uoc == 1) #True
    print(n > 1) # True
    print(f"Số {n} là số nguyên tố")
else:
    print(f"Số {n} là không phải số nguyên tố")
    
    
