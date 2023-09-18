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



DATA = game_data.data

def pick_data():
    pick = random.choice(DATA)
    name = pick["name"]
    follower_count = pick["follower_count"]
    description = pick["description"]
    country = pick["country"]
    print([name, follower_count, description, country])
    return [name, follower_count, description, country]

pick_data()