
toan = float(input("Nhập toán: "))
ly = float(input("Nhập lý: "))
hoa = float(input("Nhập hóa: "))

#Tạo/khai báo hàm (function)
#def (define) tên hàm ():
def calcArg():
    #code tính năng
    arg = (toan + ly + hoa)//3
    print(arg)
    
    
#Sử dùng/gọi hàm  
# Khi load/run chương trình  
calcArg()