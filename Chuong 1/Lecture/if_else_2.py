weight = int(input("Please input your weight of products: "))
distance = int(input("Please input your distance: "))
priceWeight = weight*20000 if weight < 3 else weight*30000
priceDistance = distance*20000 if distance < 10 else distance*30000

print("The delivery amount to be paid is:",priceWeight+priceDistance)