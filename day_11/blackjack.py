import random

# Start point for the game
def play_game():
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again == 'y':
        start_game()


def start_game():
    # Selects card for both player and computer
    def deal_cards():
        """Returns a random card frm the deck"""
        cards = [11, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def draw_cards():
        player = []
        computer = []
        is_game_over = False

        for _ in range(2):
            player.append(deal_cards())
            computer.append(deal_cards())

        while not is_game_over:
            # Calc score
            player_score = calculate_score(player)
            computer_score = calculate_score(computer)
            # Print selection
            print(f"Your cards: {player}, current score: {player_score}")
            print(f"Computer first card: {computer[0]}")

            if player_score == 0 or computer_score == 0 or player_score > 21:
                is_game_over = True
            else:
                deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
                if deal_again == 'y':
                    player.append(deal_cards())
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer.append(deal_cards())
            computer_score = calculate_score(computer)

        print(compare_score(player_score, computer_score))

        play_again = input("Do you want to play again? Type 'y' for Yes and 'n' for No: ")
        if play_again == 'y':
            start_game()

    
    def calculate_score(cards):
        """Take a list of card and return the score of calculated cards"""
        # check if hand is a blackjack
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)


    def compare_score(player_score, computer_score):
        if computer_score == player_score:
            return "Draw"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack"
        elif player_score == 0:
            return "Win with a Blackjack"
        elif player_score > 21:
            return "You went over. You lose"
        elif compare_score > 21:
            return "Opponent went over. You win"
        elif player_score > computer_score:
            return "You win"
        else:
            return "You lose"

    draw_cards()    

play_game()







# select_cards()