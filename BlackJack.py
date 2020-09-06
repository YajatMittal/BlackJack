import random
ace_value = 11

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':ace_value}

playing_game =  True
playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit,rank)
                self.deck.append(new_card)
    def __str__(self):
        for card in self.deck:
            print(card)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
       
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
    def adjust_for_ace(self):
        player_input = 0
        while player_input != 1 or player_input != 11:
            player_input = int(input("Do you want ace's value in your game to be 11 or 1? Please enter"))
        
        if player_input == 1:
            global ace_value 
            ace_value = 1
            
    def card_list(self):
        for cards in self.cards:
            print(cards)
        
        

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

chips = Chips()
def take_bet():
    
    print("Blance:{}".format(chips.total))
    while True:
        try:
            chips_bet = int(input("How much so you want to bet?"))
            if chips_bet > chips.total:
                print("Exceeded balance")
                continue

            elif chips_bet == 0:
               print("Exceeded balance")
               continue

        except:
            print("try again!")
            continue
        
        else:
            chips.bet = chips_bet
            break

deck = Deck()
hand = Hand()
def hit(deck,hand):
    deal = deck.deal()
    hand.add_card(deal)
    print()
    print("your cards:")
    hand.card_list()
    print()
    print("Value of cards:{}".format(hand.value))

def hit_or_stand():
    global playing  # to control an upcoming while loop
    while playing:
        if hand.value == 21:
            player_wins()
            playing = False

        elif hand.value > 21:
            player_busts()
            playing = False

        else:
            hit_input = str(input("Enter H to hit and S to stay"))

            if hit_input.lower() == "h":
                hit(deck,hand)

            elif hit_input.lower() == "s":
                playing = False

        
        
            else:
                print("try again!")
                continue
                
        

computer_cards = []
computer_card_value = 0

def show_some():
    global computer_cards
    global computer_card_value
    card1 = deck.deal()
    card2 = deck.deal()
    computer_card_value += values[card1.rank]
    computer_card_value += values[card2.rank]
    computer_cards = [card1, card2]
    computer_cards = [cards for cards in computer_cards]
    print("dealer's cards:")
    print(computer_cards[0])
    print("hidden card")

def show_all():            
    card1 = deck.deal()
    card2 = deck.deal()
    hand.add_card(card1)
    hand.add_card(card2)
    print("your cards:")
    hand.card_list()
    print()
    print("Value of cards:{}".format(hand.value))



def dealer_card():
    print("dealer's cards:")
    for cards in computer_cards:
        print(cards)

def player_busts():
    if hand.value > 21:
        print("You Got Bust!")
        chips.lose_bet()

def player_wins():
    if hand.value == 21:
        print("You Won!")
        chips.win_bet()

def dealer_busts():
    if computer_card_value > 21:
        print("Dealer Got Bust!")
        dealer_card()
        chips.win_bet()

def dealer_wins():
    if computer_card_value == 21:
        print("Dealer Won!")
        dealer_card()
        chips.lose_bet()

    
def push():
    print("Computer dealer and player tie")

def reset():
    global computer_cards
    global computer_card_value
    global playing
    playing = True
    hand.value = 0
    hand.cards = []
    computer_cards = []
    computer_card_value = 0
    
while playing_game:
    deck.shuffle()
    take_bet()
    print()
    print()
    show_some()
    print()
    print()
    show_all()
    print()
    while playing:
        hit_or_stand()
        

        
    if hand.value < 21 and computer_card_value < 17 and computer_card_value != 17 :                                                                          
        while computer_card_value < 17:
            card = deck.deal()
            computer_cards.append(card)
            computer_card_value += values[card.rank]
        
        if computer_card_value > 21:
            dealer_busts()

        elif computer_card_value == 21:
            dealer_wins()

        elif computer_card_value == hand.value:
            push()
    
    print()
    

    print("Your balance is now:{}".format(chips.total))
    print()
    play_again = str(input("Do you want to continue?Y/N"))
    
    if play_again == "n":
        playing_game = False
    
    reset()
    