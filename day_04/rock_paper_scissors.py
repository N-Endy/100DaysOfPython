import random

# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = [rock, paper, scissors]
# get user's choice
user = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
while user > 2:
    user = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
user_choice = choice[user]
print(f"You chose:\n{user_choice}")

# generate computer's choice
random_int = random.randint(0,2)
computer_choice = choice[random_int]
# computer_choice = random.choice(choice) Selects directly from choice list
print(f"Computer chose {computer_choice}")

# choose winner
if user_choice == computer_choice:
    print("It is a draw!")
elif user_choice == rock:
    if computer_choice == paper:
        print("Computer wins!")
    elif computer_choice == scissors:
        print("You win!")
elif user_choice == paper:
    if computer_choice == rock:
        print("You win!")
    elif computer_choice == scissors:
        print("Computer wins!")
elif user_choice == scissors:
    if computer_choice == rock:
        print("Computer wins!")
    elif computer_choice == paper:
        print("You win!")