# store to buy items from market

things = {"book":"40",
          "pen":"10",
          "pencil":"5",
          "eraser":"5",
          "marker":"20",
          "scale":"20"}

cart =[]
total = 0.0

print("---------MATERIALS---------")
for key , value in things.items():
    print(f"{key:10}:₹{float(value):.2f}")
print("---------------------------")

while True :
    item = input("select an item (q to quit) :").lower()
    if item == "q" :
        break
    elif things.get(item) is not None :
        cart.append(item)

print("---------------------------")
for item in cart :
    total += float(things.get(item))
    print(item, end = " ")

print()
print(f"total is ₹{total:.2f}")


