class PlayingCard:  # inherits from 'object'
    def __init__(self, rank, suit):
        # self is the INSTANCE
        self._rank = rank   # "private" instance variable
        self._suit = suit

    @property
    def rank(self):  # "public" instance variable AKA getter property
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    def __str__(self):
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):
        return f"PlayingCard('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = PlayingCard("8", "Diamonds")
    colors = list()
    print(c1)  # str()
    print(f"{c1 = }")   # repr()
    print(f"{c1.rank = }")  # calls PlayingCard.rank()
    print(f"{c1.suit = }")
    
    