'''
Cho người nhập vào 3 số => sắp xếp các số theo thứ tự tăng dần
input: 3,21,6
num1, num2, num3

process:
    +giả sử num3 lớn nhất:
        num1, num2, num3
        num2, num1, num3 
        
    +giả sử num2 lớn nhất:
        num1, num3, num2
        num3, num1, num2
        
    +giả sử num1 lớn nhất:
        num2,num3, num1
        num3,num2, num1

Output: 3,6,21
'''

# B1: cho user nhập 3 số nguyên
num1 = int(input("Nhập số thứ nhất 1: "))
num2 = int(input("Nhập số thứ nhất 2: "))
num3 = int(input("Nhập số thứ nhất 3: "))

#B3 kiểm tra dựa vào các trường hợp giả sử
if num1 > num2: 
    if num2 > num3:
        print(num3, num2, num1)
    else:
        if num1 > num3:
            print( num2,num3,num1)
        else:
            print(num2, num1,num3)
elif num2 > num3:
     if num3 > num1:
         print(num1, num3, num2) 
     else:
         print(num3, num1, num2) 
    
else:
    print( num1,num2,num3)