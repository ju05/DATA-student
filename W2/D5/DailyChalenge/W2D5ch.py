# What is a class?
# A blueprint for creating objects with specific attributes and methods.
#
# What is an instance?
# An individual object created from a class.
#
# What is encapsulation?
# Hiding internal state and requiring all interaction through methods.
#
# What is abstraction?
# Hiding complex implementation details and showing only essential features.
#
# What is inheritance?
# A mechanism where a class (child) can use attributes and methods from another class (parent).
#
# What is multiple inheritance?
# When a class inherits from more than one parent class.
#
# What is polymorphism?
# The ability to use a single interface for different data types or classes.
#
# What is method resolution order or MRO?
# The order in which Python looks for a method in a hierarchy of classes when using inheritance.

import random


class Card:
    def __init__(self, suit, value):
        """Initialize a new card with two attributes: suit and value."""
        self.suit = suit
        self.value = value

    def __str__(self):
        """Return a string representation of the card in a readable format."""
        return f"{self.value} {self.suit}"


class Deck:
    def __init__(self):
        """Initialize a new deck of cards and shuffle it upon creation."""
        self.cards = []
        self.shuffle()

    def shuffle(self):
        """Create a new deck of 52 cards and shuffle them using the random module."""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def deal(self):
        """Remove and return the last card from the deck. Return None if the deck is empty."""
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


deck = Deck()
print(deck.deal())
print(len(deck.cards))

