# Setup
backpack = []
total_gold = 500

weapons = ["sword", "staff"]
weapon_prices = {"sword": 150, "staff": 230}

while True:
    print("Available weapons:", weapons)
    choice = input("Choose your weapon: ")

    if choice == "sword":
        print("You have chosen a sword, that will cost you 150")
        backpack.append("sword")
        total_gold -= 150
        break  # Exit the loop after a valid choice
    elif choice == "staff":
        print("You have chosen a staff, that will cost you 230")
        backpack.append("staff")
        total_gold -= 230
        break  # Exit the loop after a valid choice
    else:
        print("We don't have that particular item, please choose again.")

print("Your backpack now:", backpack)
print("Your remaining gold:", total_gold)

