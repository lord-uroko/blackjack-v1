# This program will allow you to play blackjack
## TO DO LIST: add the ability for additional players
## To DO LIST: add loop spanning entire game
## TO DO LIST: add betting functionality

import random

# Create a Deck of cards class
class Deck:
    def __init__(self): # Build the deck
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [(value + " of " + suits) for value in self.value for suits in self.suits]
        self.cards_values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, \
                              'Jack': 10,'Queen': 10, 'King': 10}
    def select_card(self):
        if not self.cards:
            self.__init__() # Reset the deck if it's empty
            return None
        card = random.choice(self.cards)
        self.cards.remove(card)
        card_name = card.split(" of")[0]
        card_value = self.cards_values[card_name]
        return (card, card_value)
    
# Create a deck instance
deck = Deck()

def dealer_card_draw():
    return deck.select_card()

def player_card_draw():
    card_info = deck.select_card()
    if card_info:
        card, value = card_info
        print(f"You drew: {card}")
        return card_info
    else:
        print("The deck is empty.") 

def calculate_hand_value(hand):
    total = sum(value for _, value in hand)
    aces = sum(1 for card, _ in hand if card.startswith("Ace"))
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Start a game of Blackjack
print("Welcome to Blackjack!")
player_hand = [player_card_draw(), player_card_draw()]
dealer_hand = [dealer_card_draw(), dealer_card_draw()]
print(f"The dealer's show card is: {dealer_hand[1][0]}")

player_total_value = calculate_hand_value(player_hand)
dealer_total_value = calculate_hand_value(dealer_hand)

if player_total_value == 21:
    print("Blackjack off the draw! INCREDIBLE!!!")
    exit()

while True:
    choice = input("Press 'H' to hit, or 'S' to stand: ").upper()
    if choice == "H":
        player_hand.append(player_card_draw())
        player_total_value = calculate_hand_value(player_hand)
        if player_total_value > 21:
            print("Bust!")
            break
        elif player_total_value == 21:
            print("Congratulations! You win!")
            break
        else:
            print("Your new total is " + str(player_total_value))
            continue
    # End player's turn.

    elif choice == "S":
        print(f"The dealer's cards are {dealer_hand[1][0]} and {dealer_hand[0][0]}")
        print("The dealer's total is " + str(dealer_total_value))

        # while loop until the dealer has at least 17.
        while dealer_total_value < 17:
                    ###### NOT SHOWING THE NEW CARD #######
            dealer_new_draw = dealer_card_draw()
            dealer_hand.append(dealer_new_draw)
            dealer_total_value = calculate_hand_value(dealer_hand)
            print(F"The dealer drew a " + dealer_new_draw[0])
            print("The dealer's new total is " + str(dealer_total_value))

        # Win/Lose conditions.
        if dealer_total_value > 21 or (dealer_total_value <= 21 and player_total_value > dealer_total_value):
            print("You win this round!")
        else:
            print("Better luck next time!")
        print("Thanks for playing!") # change this to end the round
        break
    else:
        print("Invalid choice. Please try again.")
