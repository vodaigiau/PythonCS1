'''
Input:
    toan, ly, hoa

Process:
    B1: Yêu cầu nhập từ user
    B2: Tính điểm trung bình
        dtb = (toan + ly + hoa)/ 3
    B3: Kiểm tra xếp loại
        Nếu dtb > 9, loại A
        Ngược lại nếu 8 <= dtb <=9 (dtb lớn hơn bằng 8 và bé hơn bằng 9), loại B
        Ngược lại nếu  7 <= dtb <8, loại C
        Ngược lại nếu  5 <= dtb <7, loại D
        Ngược lại , loại E
    
Output:
    loai
'''

# B1:
toan = float(input("Nhập điểm toán: "))
ly = float(input("Nhập điểm lý: "))
hoa = float(input("Nhập điểm hóa: "))

#B2:
dtb = (toan + ly + hoa)/ 3
print(dtb)

#B3
# hệ số 10: 0 -> 10
#! Lỗi cú pháp (dùng sai ngôn ngữ)
#! Lỗi nghiệp vụ (Business logic)
if 10>= dtb > 9: #True
    print("Loại A")
elif 8 <= dtb <=9: #True
    print("Loại B")
elif 7 <= dtb <8: #True
    print("Loại C")
elif 5 <= dtb <7: #True
    print("Loại D")
elif 0 <= dtb < 5: #True
    #Ngược lại với tất cả các điều kiện trên
    print("Loại E")
else:
    # điểm > 10 , điểm < 0
    print("Điểm trung bình không đúng")