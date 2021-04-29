import random
import turtle
import os
os.system("clear")
print("GO FISH\n\n")

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
        self.suits = ['H', 'D', 'S', 'C']
        self.values = ['A','K','Q','J','2','3','4','5','6','7','8','9']
        
        for suit in self.suits:
            for value in self.values:
                card = Card(suit, value)
                self.cards.append(card)
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def get_card(self):
        return self.cards.pop()
        
    def discard(self):
        return self.cards.pop()
        
class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []
        self.guess = False
        self.paired_cards = []
        
    def print_hand(self):
        for card in self.hand:
            print(card.value, card.suit)
            

class Enemy():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []
        self.guess = False
        self.paired_cards = []
        
    def print_hand(self):
        for card in self.hand:
            print(card.value, card.suit)
            

# Create objects
deck = Deck()
deck.shuffle()


player = Player(input("Input your name: "))
enemy = Player(input("Input the enemy's name: "))

for _ in range(7):
    card = deck.get_card()
    player.hand.append(card)
    
for _ in range(7):
    card = deck.get_card()
    enemy.hand.append(card)
    
print("Player hand")
player.print_hand()

print("Enemy hand")
enemy.print_hand()


def play():
    turn = 0
    size = 7
    deal = 0
    player_score = 0
    enemy_score = 0
    players = [player, enemy]
    
        
    # Print header
    print(f"Player: {player.score}")
    print(f"Enemy: {enemy.score}")

    # First player goes
    # Check for own pair
    # If there is a pair, place it down
    print("Check for matches in player hand.")
    match = False
    for i in range(0, len(player.hand)):
        for j in range(i+1, len(player.hand)):
            if player.hand[i].value == player.hand[j].value:
                print("MATCH")
                print("Player hand")
                match = True
                break
        if match:
            break
            
    if match:
        match1 = player.hand[i]
        match2 = player.hand[j]
        player.paired_cards.append(match1)
        player.paired_cards.append(match2)
        player.hand.remove(match1)
        player.hand.remove(match2)
        player.print_hand()
        player_score += 1
                
    if not match:
        print("NO MATCH")
        player.print_hand()
        player_guess = input("(Player) Enter your guess: ").upper()
        card_found = False
        for card in enemy.hand:
            if player_guess == card.value:
                card_found = True
                break
        
        if card_found == True:
            print("The card exists you guessed right")
            enemy.hand.remove(card)
            player.hand.append(card)
        else:
            print("You guessed wrong")
            player.hand.append(deck.get_card())
        
                
    # The other player guesses
    # If the guess is right, the other player gets one card and puts them down
    # Guess card other player has
    # If correct take care from other player
    # If not correct, player takes card from deck
    #print("ENEMY TURN TO BE CODED LATER")
    print("Check for matches in player hand.")
    match = False
    for i in range(0, len(enemy.hand)):
        for j in range(i+1, len(enemy.hand)):
            if enemy.hand[i].value == enemy.hand[j].value:
                print("MATCH")
                print("Enemy hand")
                match = True
                break
        if match:
            break
            
    if match:
        match1 = enemy.hand[i]
        match2 = enemy.hand[j]
        enemy.paired_cards.append(match1)
        enemy.paired_cards.append(match2)
        enemy.hand.remove(match1)
        enemy.hand.remove(match2)
        enemy.print_hand()
        enemy_score += 1
                
    if not match:
        print("NO MATCH")
        enemy.print_hand()
        enemy_guess = random.choice(deck.values)
        card_found = False 
        for card in player.hand:
            if enemy_guess == card.value:
                card_found = True
                break
        
        if card_found == True:
            print("The enemy guessed right.")
            player.hand.remove(card)
            enemy.hand.append(card)
        else:
            print("The enemy guessed wrong.")
            enemy.hand.append(deck.get_card())
            
    input()
        
    if len(player.hand) == 0:
        print("Player wins. Game over")
        exit()    
    elif len(enemy.hand) == 0:
        print("Enemy wins. Game over")
        exit()
    
    if len(player.paired_cards) > len(enemy.paired_cards):
        print("You have more paired cards than the enemy.") 
    
    elif len(enemy.paired_cards) > len(player.paired_cards):
        print("The enemy has more paired cards than the player.")
    
    play()
                
play()


#last thing to add in is images/sound
