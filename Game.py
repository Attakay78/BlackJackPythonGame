from sys import argv

from Suits import Suit
from Face import Face
from random import shuffle

def createDeck() -> list:
    deck : list = []

    for suit in Suit:
        for face in Face:
            deck.append((int(face.value), suit.name))
    
    return deck


def createDeck() -> list:
    return [(int(face.value), suit.name) for suit in Suit for face in Face]


def shuffleDeck() -> list:
    new_deck : list = createDeck()
    shuffle(new_deck)
    return new_deck

