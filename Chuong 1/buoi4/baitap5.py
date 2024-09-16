'''

số bị chia / số chia
n = 7 (số nguyên tố)
=> 7/1, 7/2, 7/3, 7/4, 7/5, 7/6, 7/7
+ ước số: 2 ước (1 & 7)

n = 10 (không phải)
=> 10/1, 10/2, 10/3, 10/4, 10/5, 10/6, 10/7, 10/8, 10/9, 10/10
+ ước số: 4 ước (1,2,5,10)


Kết luận:
- snt: số chỉ có 2 ước
- số chia tăng dần (+ 1)
- so_chia <= n => tiếp tục, ngược lại > n => dừng 

'''

#? B1:
n = int(input("Nhập số n: "))
#? B2: xác định giá trị biến cần đổi
so_chia = 1
so_luong_uoc = 0
count = 0

#? B3:điều kiện lặp
while so_chia <= n:
    #? B4: code cần lặp
    if n % so_chia == 0:
        # chia hết
        so_luong_uoc +=1
    #? B5: tăng giá trị của biến so_chia
    so_chia +=1
    count +=1 
    
print(count)  
if so_luong_uoc == 2:
    print(f"Số {n} là số nguyên tố")
else:
    print(f"Số {n} là không phải số nguyên tố")
    
    
    

