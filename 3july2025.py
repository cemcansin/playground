male_warrior_names = ["Lucien", "Axel", "Dougles", "Laos"]
female_warrior_names = ["Fiora", "June", "Opal", "Sylvana"]
classes = ["Warrior", "Mage", "Druid", "Ranger"]

picked_gender = input("Pick a gender (Male or Female): ").capitalize()

if picked_gender == "Male":
    name_list = male_warrior_names
elif picked_gender == "Female":
    name_list = female_warrior_names
else:
    print("Not a valid gender. Exiting.")
    exit()

print("Here are the names available:")
for i, name in enumerate(name_list):
    print(f"{i + 1}: {name}")

print("Choose your name by number:")
choice_index = int(input()) - 1

if 0 <= choice_index < len(name_list):
    picked_name = name_list[choice_index]
    print(f"You picked: {picked_name}")
else:
    print("Invalid choice. Exiting.")
    exit()





