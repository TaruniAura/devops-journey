inventory ={
    "Laptop":10,
    "Mouse":25,
    "Keyboard":15
}

print("Availbale items")

for item,stock in inventory.items():
    print(item,":",stock)

item=input("Enter the item: ")

if item in inventory:
    print("Stock:", inventory[item])
else:
    print("item not found")    