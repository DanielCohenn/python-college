import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f'Deck of {len(self.cards)} cards'

    def count(self):
        return len(self.cards)

    def deal(self, number_to_deal):
        if number_to_deal < len(self.cards) or number_to_deal == len(self.cards):
            hand = self.cards[-number_to_deal:]
            self.cards = self.cards[:-number_to_deal]
            return hand
        elif len(self.cards) == 0:
            raise ValueError('All cards have been dealt')
        elif len(self.cards) < number_to_deal:
            actual = min(number_to_deal, len(self.cards))
            hand = self.cards[-actual:]
            self.cards = self.cards[:-actual]
            return hand

    def shuffle(self):
        new_list = self.cards
        if self.count() == 52:
            self.cards = random.sample(new_list, len(new_list))
            return self.cards
        raise ValueError('Deck is not full')

    def deal_card(self):
        return self.deal(1)[0]

    def deal_hand(self, num):
        return self.deal(num)



