mathMark = float(input("Nhap diem toan:"))
physicsMark = float(input("Nhap diem ly:"))
chemistryMark = float(input("Nhap diem hoa:"))
avgMark = (mathMark+physicsMark+chemistryMark)/3
if avgMark > 9:
    print("A")
elif 8 <= avgMark <= 9:
    print("B")
elif 7 <= avgMark <= 8:
    print("C")
elif 5 <= avgMark <= 7:
    print("D")
elif 0 <= avgMark <= 5:
    print("E")
elif avgMark < 0:
    print("diem khong hop le")
