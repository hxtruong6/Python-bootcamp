import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    def __init__(self, _suit, _rank):
        self.suit = _suit
        self.rank = _rank
        self.value = values[self.rank]

    def __str__(self):
        return (f"{self.rank} of {self.suit}")



class Deck:
    def __init__(self):
        self.deck = []  #init a list of Cards
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp+= '/n' + card.__str__()
        return "There deck has: "+ deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, _card):
        self.cards.append(_card)
        self.value += values[_card.rank]
        if (_card.rank== "Ace"):
            self.aces += 1

    def adjust_for_ace(self):
        while self.aces and self.value > 21:
            self.value -= 10 # -11 + 1
            self.aces -= 1

class Chips:
    def __init__(self, defaulMoney = 100):
        self.total = defaulMoney
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Function to get bet money
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter your bet money: "))
        except:
            print("Error! Please enter an number!\n")
            continue
        else:
            if (chips.bet > chips.total):
                print("Sorry! You don't have enough money to bet. You have: {}".format(chips.total))
            else:
                break

# Function to hit a card from Deck then put it into Hand
def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

# Function to control player hit or stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        userInput = input("Hit, Stand or Calculate sum of hand? Enter h, s or c: ")

        if userInput[0].lower() == 'h':
            hit(deck,hand)
        elif userInput[0].lower() == 's':
            print("Player Stand dealer's Turn")
            playing = False
        elif userInput[0].lower() == 'c':
            print("Total of hand: {}".format(hand.value))
        else:
            print("Sorry! It's wrong format. Please just enter h or s: ")
            continue
        break


# Function to display the cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

# Functions to handle end of game scenarios
def player_busts(player,dealer,chips):
    print("Bust Player")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Plyer wins! Dealer busted")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins")
    chips.lose_bet()

def push(player,dealer):
    print("Player and Dealer tie! PUSH")

# Main function
if __name__ == "__main__":
    # Print an opening statement
    print("Welcome to BlacJack!!!")
    # Set up the Player's chips
    player_chips = Chips()
    print("Player has: {}$".format(player_chips.total))

    while True:
        # Prompt the Player for their bet
        take_bet(player_chips)
        print("Player has: {}$ remain".format(player_chips.total))
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)

        # Inform Player of their chips total
        print("\nPlayer's winnings stand at",player_chips.total)
        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        if new_game[0].lower()=='y':
            playing=True
            continue
        else:
            print("Thanks for playing!")
            break
