# win-ctrl + /, mac - cmd + /  : chuyển 1 đoạn chữ thành ghi chú
# in thông báo 1 đoạn chữ
#TODO: Nhớ lưu file code (ctrl + s : save file)
print("Hello CS Foundation")

#? Làm sao lưu được các thông tin ở ngôn ngữ lập trình (trong máy tính)?
#TODO: Variable (Biến): Lưu dữ liệu trong lập trình
#1. Cách tạo biến (Khai báo biến)
# Tên biến = giá trị/dữ liệu
fullname = "Vo Dai Giau"

#2. Sử dụng biến (Gọi biến)
# print(fullname)

#TODO: tạo 1 biến chứa tin nhắn, in tin nhắn 
#? Kiểu dữ liệu => quy định rõ ràng dữ liệu => sử dụng phù hợp trong tính toán
#string: chuỗi ký tự => đặt trong dấu "string"
tin_nhan = "Hello"
print(tin_nhan, fullname)

#? number: số nguyên(int: 2,1,3,4,10...), số thực (float: 9.25, 9.5)
age = 20
print(age)

#TODO: Sử dụng lệnh nhập - Cho phép người dùng nhập tên , lưu vào biến, in kết ra
# đọc code từ bên phải dấn gán (=) trước => sau đó đọc bên trái
# your_name = input("Vui lòng nhập tên: ") # Nhập tên từ người dùng sau đó gán(lưu) vào biến có tên là your_name

# print("Tên của bạn là: ", your_name)


#TODO: cho nguoi dùng nhập 2 số, tính tổng 2 số và in kết quả
#B1: tạo 2 biến chứa 2 số, cho user nhập từng số
# 1 + 1 => 11
# 2 + 4 => 24
num1 = input("Nhập số thứ nhất: ") #luôn là kiểu string
num2 = input("Nhập số thứ hai: ")

#Nguyên nhân
print(type(num1)) #kiểm tra kiểu dữ liệu
#String
print("a"+"b") # dấu + đi với kiểu string sẽ dùng ghép chuỗi
print("1" + "1") # 11


#B2: tính tổng
#Chuyển kiểu từ chữ sang số (ép kiểu)/ convert data type
#! int(num1 + num2): công trước => chuyển kiểu
sum = int(num1) + int(num2) #chuyển string sang int

#B3: in kết quả
print("Tổng 2 số là: ", sum)