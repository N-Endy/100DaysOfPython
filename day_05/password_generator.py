#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
password_array = []
# Loop through lists and make a random choice and append to password_array
for letter in range(0, nr_letters):
    password_array.append(random.choice(letters))

for number in range(0, nr_numbers):
    password_array.append(random.choice(numbers))

for symbol in range(0, nr_symbols):
    password_array.append(random.choice(symbols))
# loop through password_array list and make choice
# loop through password_array, extract item from list and add to string password
while len(password_array) > 0:
    random_int = random.randint(0, (len(password_array) - 1))
    password += password_array.pop(random_int)

print(f"Your password is {password}")