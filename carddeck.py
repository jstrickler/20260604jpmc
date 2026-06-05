import random
from playingcard import PlayingCard

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = PlayingCard(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()


if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    names = list()
    colors = list()
    d1.shuffle()
    print(f"{d1.cards = }")
    for _ in range(5):
        card = d1.draw()
        print(f"{card = }")
        