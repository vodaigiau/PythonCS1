'''
Phép toán của kiểu Boolean
True/False

and 
n = 3
True and True => True
=> Tất cả kết quả so sánh là True 
=> đáp án cuối là True

n = 1
True and False => False
True and False and True=> False

or
TH1: 21 (tổng 2 lá bài) => True
Th2: Ngũ tiên (tổng 5 lá <= 21) => True
Th3: lá bài <= 21 and lớn hơn cái => True

TH1 or TH2 or TH3  
True or False or False => True
False or False or False => False

Ngôn ngữ khác python
and : &&
or: ||
'''

print(True and True and True) #True
print(True and True and False) #False

print(True or False or False) #True
print(False or False or False)#False