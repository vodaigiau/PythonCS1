
#TODO: Cho người dùng nhập độ C, chuyển sang độ F
# F = C x 59 + 32 (công thức vật lý)

#? IPO: mô hình 3 khối
# B1: Cho người dùng nhập độ C
celsius =  input("Nhập độ C: ") # luôn là string

#B2: Lập công thức
#? cần chuyển do_c từ string sang kiểu số , dùng float vì nhiệt độ có thể nhập số thực
farenheit = float(celsius) * 59 + 32 

#B3: in kq
print("Độ F là: ", farenheit)