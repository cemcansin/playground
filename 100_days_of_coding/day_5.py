#for number in range(1, 101):
#    if number %5 == 0 and number %3 == 0:
#        number = "FizzBuzz"
#    elif number %3 == 0:
#        number = "Fizz"
#    elif number %5 == 0:
#        number = "Buzz"
#   print(number)

import random
import string

letters = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

nr_letters = int(input(f"How many letters do you want in your password\n"))
nr_numbers = int(input(f"How many numbers do you want in your password\n"))
nr_symbols = int(input(f"How many symbols do you want in your password\n"))

password_list = []
for char in range (0, nr_letters):
    password_list += random.choice(letters)
for char in range (0, nr_numbers):
    password_list += random.choice(numbers)
for char in range (0, nr_letters):
    password_list += random.choice(symbols)
random.shuffle(password_list)
print(password_list)
password = ""
for i in password_list:
    password += i
print(f"Your password is {password}")


