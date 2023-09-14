import random
import hangman_art
import hangman_words

print(hangman_art.logo)
display = []
# randomly choose a word from the word_list
chosen_word = random.choice(hangman_words.word_list)
# generate word has being hidden
for i in chosen_word:
    display.append("_")

# keep track of unguessed letters
unguessed = 0
for _ in display:
    if _ == "_":
        unguessed += 1

life = 6

# ask user to guess a letter
while unguessed > 0 and life > 0:
    guess = input("Choose a letter for the word: ").lower()
    
    # alert user on already chosen word
    if guess in display:
        print(f"You have already guessed letter {guess}")

    # check if the guessed letter is in the word
    for idx, letter in enumerate(chosen_word):
        if guess == letter:
            display[idx] = letter
            unguessed -= 1
    print(" ".join(display))

    if guess not in chosen_word:
        life -= 1
        print(hangman_art.stages[life])
        print(f"You guessed {guess}, that's not in the word. You lose a life")

if life == 0:
    print(f"You lose! The word was {chosen_word}")
else:
    print("Congratulations! You win!")