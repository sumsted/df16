""" All possible items and monsters are kept here.
These are imported into room when building each room object.

ITEMS - list of dictionaries containing
  name - name of the room
  attack - number of points deducted from monster during attack
  health - number of points added to player if eaten


MONSTERS - list of dictionaries containing
  name - name of monster
  attack - number of points deducted from player during counter attack
  health - starting health of monster

"""
STARTING_ITEM = 0


ITEMS = [
    {'name': 'spoon', 'attack': 1, 'health': -1},
    {'name': 'sword', 'attack': 30, 'health': -1},
    {'name': 'messenger bag', 'attack': 10, 'health': 4},
    {'name': 'skinny jeans', 'attack': 1, 'health': 1},
    {'name': 'beard trimmer', 'attack': 30, 'health': 3},
    {'name': 'mac book pro', 'attack': 15, 'health': 10},
    {'name': 'conference badge', 'attack': 15, 'health': 2},
    {'name': 'tall latte', 'attack': 20, 'health': 1},
    {'name': 'session speaker', 'attack': 20, 'health': 2},
    {'name': 'keynote speaker', 'attack': 30, 'health': 4},
    {'name': 'new raccoon suit', 'attack': 5, 'health': 4},
    {'name': 'water bottle', 'attack': 20, 'health': 2},
    {'name': 'iphone', 'attack': 30, 'health': 1},
    {'name': 'pizza', 'attack': 2, 'health': 30},
    {'name': 'noodles', 'attack': 2, 'health': 10},
    {'name': 'skittles', 'attack': 2, 'health': 10},
    {'name': 'unicorn', 'attack': 20, 'health': 30},
    {'name': 'chicken', 'attack': 0, 'health': 10},
    {'name': 'red bull', 'attack': 5, 'health': 50}
]


MONSTERS = [
    {'name': 'Grover', 'attack': 1, 'health': 5},
    {'name': 'Elmo', 'attack': 2, 'health': 10},
    {'name': 'Cookie Monster', 'attack': 8, 'health': 20},
    {'name': 'Big Bird', 'attack': 10, 'health': 30},
    {'name': 'Potato Man', 'attack': 6, 'health': 20},
    {'name': 'Peanutbot', 'attack': 5, 'health': 12},
    {'name': 'Count von Count', 'attack': 10, 'health': 30},
    {'name': 'Ernie', 'attack': 5, 'health': 12},
    {'name': 'Bert', 'attack': 5, 'health': 12},
    {'name': 'Kermit', 'attack': 5, 'health': 5},
    {'name': 'Herry the Monster', 'attack': 20, 'health': 20}
]
