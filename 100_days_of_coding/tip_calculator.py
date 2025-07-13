print("Welcome to tip calculator")
total_bill = int(input("What was the total bill\n"))
pref_tip = int(input("How much tip would you like to give"))
people = int(input("How many people are paying"))
tip = pref_tip / 100 * total_bill + total_bill
a = round(tip / people)
print(f"The total with the tip is {tip}")
print(f"Each person should pay {a}")