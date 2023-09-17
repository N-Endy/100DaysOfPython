# load game
# show prompt
# prompt for input; easy or hard
# allocate life based on difficulty
# prompt for guess
# IF guess is less than num
    # reduce life by 1
    # prompt will too low
    # IF life is equal to zero
        # end game
# ELSE IF guess is greater than 1
    # reduce life by 1
    # prompt too high
    # IF life is equal to zero
        # end game
# ELSE IF guess is equal to number
    # prompt win
    # end game

# FUNCTIONS
# load_game
# prompt-message
# easy_mode
# hard_mode
# check_life
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    hidden_num = random.randint(1, 100)

    def choose_difficulty(level):
        if level == "easy":
            return 10
        elif level == "hard":
            return 5
        

    def get_life():
        """Returns the quantity of life based on user choice of difficulty"""

        # prompt for difficulty choice
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        
        return choose_difficulty(difficulty)


    def guess_number():
        user_guess = int(input("Make a guess: "))
        return user_guess    


    def play_again():
        prompt = input("Would you like to play again? 'yes' or 'no': ")
        if prompt == "yes":
            start_game()
        else:
            print("Thank you for playing")


    def check_life(life):
        if life == 0:
            print(f"You have run out of lives. You lose. The number was {hidden_number}")            play_again()
        else:
            print(f"You have {life} attempts remaining to guess the number")


    def check_guess():
        user_life = get_life()
        while user_life > 0:
            number = guess_number()
            if number < hidden_num:
                user_life -= 1
                print("Number is too low")
                check_life(user_life)
            elif number > hidden_num:
                user_life -= 1
                print("Number too high")
                check_life(user_life)
            else:
                print(f"Congratulations! You've guessed the number {hidden_num} correctly!")
                play_again()
                break  # Exit the loop after a correct guess

    check_guess()

start_game()