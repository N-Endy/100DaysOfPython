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

def pick_data():
    pick = random.choice(DATA)
    name = pick["name"]
    follower_count = pick["follower_count"]
    description = pick["description"]
    country = pick["country"]
    return [name, follower_count, description, country]

def compare_celebrity():
    celeb_a = pick_data()
    celeb_b = pick_data()
    while celeb_b[0] == celeb_a[0]:
        celeb_b = pick_data()


    print(f"Compare A: {celeb_a[0]}, a {celeb_a[2]}, from {celeb_a[3]}")
    print({VS})
    print(f"Compare B: {celeb_b[0]}, a {celeb_b[2]}, from {celeb_b[3]}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    while answer != "a" and answer != "b":
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    check_compare(celeb_a, celeb_b, answer)

def check_compare(data1, data2, input):
    score = 0
    if input == "a" and data1[1] > data2[1]:
        score +=1
        print(f"You are right! Current Score: {score}")
    elif input == "a" and data1[1] < data2[1]:
        print(f"Sorry, that's wrong. Final Score: {score}")
    elif input == "b" and data2[1] > data1[1]:
        score +=1
        print(f"You are right! Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")

compare_celebrity()

