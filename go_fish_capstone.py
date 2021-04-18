import random
import turtle
import os
os.system("clear")

wn = turtle.Screen()
wn.title("Go Fish")
wn.bgcolor("black")
wn.setup(600,800)
wn.tracer(0)


#52 cards, 13 of each suit (clubs, diamonds, hearts, and spades)

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        if suit == "H" or suit == "D":
            self.color = "R"
        else:
            self.color = "B"
        self.value = value
        
class Deck():
    def __init__(self):
        self.cards = []
        suits = ['H', 'D', 'S', 'C']
        values = ['A','K','Q','J','2','3','4','5','6','7','8','9']
        
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card)
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def get_card(self):
        return self.cards.pop()
    
class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []
        self.guess = False
        
class Enemy():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []
        self.guess = False

# Create objects
deck = Deck()
deck.shuffle()


player = Player("Khadeeja")
enemy = Enemy("Rukaiya")

for _ in range(7):
    card = deck.get_card()
    player.hand.append(card)
    
for _ in range(7):
    card = deck.get_card()
    enemy.hand.append(card)
    
for i in range(7):
    card = player.hand[i]
    print(card.suit, card.value)

for i in range(7):
    card = enemy.hand[i]
    print(card.suit, card.value)

    
def play(player,enemy,deck):
    turn = 0
    size = 7
    deal = 0
    order = [player, enemy]
    
    while len(deck) != 0:
        for player in order:
            hand = player.name + "'s hand"
            for card in player.hand:
                hand += random.card
                
                
            
                
        



#last thing to add in is images/sound
