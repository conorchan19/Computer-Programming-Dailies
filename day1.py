# write a function that traverses a list and returns a random name from said list
# bonus if you write in nested loops for traversal, concatenation of results, etc.

from random import randint

def favorite_raider_player():
    players = ["Maxx Crosby", "Ashton Jeanty", "Jakobi Meyers", "Brock Bowers", "Geno Smith", "Malcolm Koonce",  "Kolton Miller"]
    random = randint(0, len(players) - 1)
    print(players[random])

favorite_raider_player()
