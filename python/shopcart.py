# to create a shopping cart program using list

foods = []
prices = []
total = 0

while True :
    food = input("enter a food to buy (press q to quit) :")
    if food.lower() == "q" :
        break
    else :
        price = float(input(f"enter the price of {food} : $"))
        foods.append(food)
        prices.append(price)

print("-------YOUR CART-------")

for food in foods :
    print(food, end =" ")

for price in prices :
    total += price

print(f" your total is :${total:.02}")    
