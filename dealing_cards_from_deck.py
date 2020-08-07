import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K']


class Card:
    """"
    the suit represents one of the categories into
    which the cards in a deck are divided.
    the value represent the number 1 (ace) trough K(king).
    """
    def __init__(self, suit, value: str):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    """
    the class Deck takes the cards represent in class Cards
    and put every combination (52 cards) in a list form with
    the cards as string.
    example: ['A of hearts',...]
    """
    def __init__(self):
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def __repr__(self):
        # shows how many cards are in the deck with a string
        return f'Deck of {len(self.cards)} cards'

    def count(self):
        # counting the number of cards in our deck
        return len(self.cards)

    def deck(self):
        return self.cards

    def deal(self, number_to_deal: int):
        """
        the function deal gets as an input the variable
        number_to_deal (always integer) and deal the number of cards on
        to a variable called hand, the hand variable represents the cards that
        were dealt to your hand, also the deck updates after we deal the cards.
        if there are no more cards in deck we print as an error.
        """
        hand = []
        while number_to_deal > 0:
            try:
                hand.append(self.cards[0])
                self.cards.pop(0)
                number_to_deal = number_to_deal - 1
            except :
                if len(self.cards) == 0:
                    print('there are no more cards in the deck')
                else:
                    print(f"we ran out of cards, you need {number_to_deal} cards more")
                break
        return hand

    def return_cards(self, number_to_return: int, hand):
        """
        this function returns random cards from hand to
        self.cards (our deck), number_to_return represents the
        number of random cards we return to our deck.
        """
        counter = 1
        while counter <= number_to_return:
            self.cards.append(hand[number_to_return])
            counter += 1
        return self.cards

    def shuffle(self):
        # this function shuffle our deck
        new_list = self.cards
        if self.count() == 52:
            self.cards = random.sample(new_list, len(new_list))
            return self.cards
        raise ValueError('Deck is not full')

    def deal_card(self):
        # this function give us the first cards from the deck
        return self.deal(1)[0]

    def deal_hand(self, num):
        # takes a number and deal the number of cards to hand
        return self.deal(num)


"""
input/output example:
my_deck = Deck() /to generate a deck
 
"""

