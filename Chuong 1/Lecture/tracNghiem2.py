# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#          print( j, end=" ")
#     print()

# array1 = [1,2,3,4]
# array2 = [5,6,7,8]
# sum_array = []
# for i in range(len(array1)):
#     sum_value = array1[i] + array2[i]
 
#     sum_array.append(sum_value)

# print(sum_array)

# n = 10
# i = 1
# while i <= n:
#     if i % 2 != 0:
#         print(i)
#     i += 1

number = 5
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(factorial)