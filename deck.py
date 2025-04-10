import random

from card import Card

class Deck:
    def __init__(self):
        self.deck = []
        suits = ["♠️", "♥️", "♦️", "♣️"]
        values = ["A"] + [i for i in range(2, 11)] + ["J", "Q", "K"]

        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

        self.shuffle(self.deck)
    
    def shuffle(self, cards):
        random.shuffle(cards)

    def draw(self):
        return self.deck.pop() if self.deck else None
        