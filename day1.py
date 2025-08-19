# write a function that traverses a list and returns a random name from said list
# bonus if you write in nested loops for traversal, concatenation of results, etc.

# imports random
from random import randint

# function definition
def favorite_raider_player():
    players = ["Maxx Crosby", "Ashton Jeanty", "Jakobi Meyers", "Brock Bowers", "Geno Smith", "Malcolm Koonce",  "Kolton Miller"] # list with raider players
    random = randint(0, len(players) - 1) # gets a random from 0 to the amount of outcome there are
    print(players[random]) # prints a random player

# function call
favorite_raider_player()

