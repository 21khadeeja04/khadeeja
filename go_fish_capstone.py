import random
import turtle
import os
os.system("clear")

wn = turtle.Screen()
wn.title("Go Fish")
wn.bgcolor("black")
wn.setup(600,800)
wn.tracer(0)

#score
score = 0

#52 cards, 13 of each suit (clubs, diamonds, hearts, and spades)

class Card():
    def __init__(self, suit, value):
        self.suit = suit
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
            
deck = Deck()

for card in deck.cards:
    deck =(card.value, card.suit)
    print(card.value, card.suit)

user_deck = deck
enemy_deck = deck




#heading for pen
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.goto(0, 250)
pen.hideturtle()
pen.write("Go fish", move = False, align = "center", font = ("Arial", "32", "normal"))

#creating the card
player = turtle.Turtle()
player.color("white")
player.shape("square")
player.speed(0)
player.penup()
player.setheading(90)
player.goto(0, -275)
player.dx = 0
        
while True:
    wn.update()



#last thing to add in is images/sound
