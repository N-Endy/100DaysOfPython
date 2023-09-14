import random
# get names from input and seperate them in a list
names_string = input("Give me everybody's names, seperate by a comma: ")
names = names_string.split(", ")

# get the length of the list
names_length = len(names)
# generate a random number from 0 to minu 1 of list length
random_int = random.randint(0, (names_length - 1))
# get random name
random_name = names[random_int]
# print message
print(f"{random_name} is paying the bill")