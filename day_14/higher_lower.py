# load ascii art for game
# load prompt for compare and Against, A and B
# Prompt for pick
# IF wrong, game ends
# ELSE
    # score is updated
    # prompt message
    # A becomes B
    # new data loaded for B
    # prompt choice again

import random
import game_data
import  art



DATA = game_data.data
LOGO = art.logo
VS = art.vs
score = 0

def pick_data():
    return random.choice(DATA)

def compare_celebrity(celeb=False):
    celeb_a = celeb
    if celeb_a == False:
        celeb_a = pick_data()
    celeb_b = pick_data()
    while celeb_b['name'] == celeb_a['name']:
        celeb_b = pick_data()


    print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}")
    print(VS)
    print(f"Compare B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    while answer != "a" and answer != "b":
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    check_compare(celeb_a, celeb_b, answer)


def check_compare(data1, data2, input):
    global score
    if (input == "a" and data1['follower_count'] > data2['follower_count']):
        score +=1
        print(f"You are right! Current Score: {score}")
        compare_celebrity(data1)
    elif input == "b" and data2['follower_count'] > data1['follower_count']:
        score +=1
        print(f"You are right! Current Score: {score}")
        compare_celebrity(data2)
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")

compare_celebrity()

