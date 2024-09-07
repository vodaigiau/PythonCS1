'''
Chương trình tự động điều chỉnh nhiệt độ
Input:
    tem (độ nhiệt)
Process:
    B1: Yêu cầu nhập nhiệt độ từ user
    B2: kiểm tra so sánh tem > 25
        Nếu tem lớn hơn 25 (True), mở điều hòa
        Ngược lại, bé hon 25 (False), tắt điều hòa
Output:
    điều chỉnh tắt/ mở điều hòa
'''

# B1:
tem = float(input("Nhập nhiệt độ"))

#B2:
if tem > 25: #True
    print("Mở điều hòa")
else: #False
    print("Tắt điều hòa")
    