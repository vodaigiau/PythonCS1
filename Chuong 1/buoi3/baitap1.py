'''
Số chẵn là số chia hết cho 2
Input:
  1 số nguyên - num (int)

Process:
    B1: Yêu cầu user nhập sô nguyên
    B2: Lấy phân dư (%) phan_du = num % 2
    B3: Kiểm tra phần dư của phép toán chia cho 2
        Nếu phần dư == 0, chia hết => số chẵn
        Ngược lại, chia không hết => số lẻ

Output:
    số chẵn / số lẻ
'''

# B1
num = int(input("Nhập số nguyên: "))

#B2:
du = num % 2

#B3:
if du == 0:#True
    print("Số chẵn nè")
else:
    print("Số lẻ")
    
    
# if num % 2 == 0:#True
#     print("Số chẵn nè")
# else:
#     print("Số lẻ")