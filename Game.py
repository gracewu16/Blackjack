import random
suits = ['',''] # Feel free to use these symbols to represent the different suits
class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.suit}, {self.rank}" # outputs the card's suit & rank/value
    
class CardCollection(object):
    def __init__(self):
        self.cards = [] # create an empty list of cards 
    def add_card(self, card):
        self.cards.append(card) # append card to the list of cards
    def draw_card(self):
        if not self.cards: # if the list of cards is empty
            raise ValueError # raises ValueError because no card can be drawn
        return self.cards.pop() # remove the most recent card in the stack/list of cards
    def make_deck(self):
        suits = ["\u2661","\u2664", "\u2662", "\u2667"] # these are the unicodes for the different symbols
        # white heart, white spade, white diamond, and white club respectively
        ranks = ['A', '1','2','3','4','5','6','7','8','9','J','K','Q'] # possible rank values
        self.cards = [Card(suit,rank) for suit in suits for rank in ranks] 
        # creates a cards with each possible combination of suit & rank
        deck = random.shuffle(self.cards) # randomly shuffles the deck of cards
    def value(self):
        valueofdeck = 0 # initial value of deck is set to zero 
        ace_count = 0 # number of aces starts at zero
        for card in self.cards: 
            if card.rank in ['J', 'Q', 'K']: # if the card has rank of J, Q, or K
                valueofdeck += 10 # value of deck increases by 10
            elif card.rank == 'A':  # aces are initially treated as 11
                ace_count += 1
                valueofdeck += 11
            else:  # Numeric cards
                valueofdeck += int(card.rank)
    # adjust aces if the total exceeds 21
        while valueofdeck > 21 and ace_count > 0:
            valueofdeck -= 10  # convert one ace from 11 to 1
            ace_count -= 1  # decrement the ace count
        return valueofdeck # return deck value
def main():
    deck = CardCollection() 
    deck.make_deck() # initialize a fresh deck of all cards
    player_hand = CardCollection()
    while True:
        # checks if the deck is empty
        if not deck.cards: # if the deck IS empty
            print("The deck is empty! The game cannot continue.")
            return # breaks the function 
        
        # player draws a card
        card = deck.draw_card() # draw first card for the player
        player_hand.add_card(card) # add the card to the player's hand
        print(f"You drew {card}.") # output the player's card to the player so they know what they drew
        
        # show the current sum
        player_sum = player_hand.value() # make player_sum equal to the value of the player's hand (based on the card's rank value)
        print(f"The sum of your hand: {player_sum}") # outputs player's hand sum
        
        # check if the player has won or lost
        if player_sum == 21: # if the player's hand ever equals 21, then they win
            print("Blackjack! You win.")
            return
        elif player_sum > 21: # if the player's hand exceeds 21, they lose
            print("Bust! You lose.")
            return
        
        # ask the player if they want another card
        another_card = input("Do you want another card? (y/n): ").strip().lower() # after  each draw that does not
        # result in ==21 or >21, prompts the player to choose if they want another card
        if another_card != 'y': # if they do, then 
            break
    
    # Dealer's turn
    print("My turn.")
    dealer_hand = CardCollection()
    
    while True:
        # checks if the deck is empty
        if not deck.cards:
            print("The deck is empty! The game cannot continue.")
            return
        
        # dealer draws a card
        card = deck.draw_card() # draws card from deck
        dealer_hand.add_card(card) # add card to dealer's hand
        print(f"I drew {card}.") 
        
        # Show the dealer's sum
        dealer_sum = dealer_hand.value() # add value of the card to dealer's hand value
        print(f"The sum of my hand: {dealer_sum}")
        
        # check if the dealer wins, loses, or continues
        if dealer_sum > 21: # if the dealer's hand exceeds 21
            print("I busted! You win.") # they lose / bust
            return
        elif (dealer_sum == 20 or dealer_sum == 21): # if the dealer's hand is equal to 20 or 21, they stay 
            break
        elif (dealer_sum >= 16 and dealer_sum < 20): # if the dealer's hand is between 16 and 19, inclusive
            if random.random() <= 0.33: 
                print ("I have decided not to pick another card") # dealer may choose to stay
                break  # dealer stays 33% of the time
    
    # Final comparison
    player_sum = player_hand.value() # final summation of the player's hand
    dealer_sum = dealer_hand.value()# final summatino of the dealer's hand
    print(f"Your sum: {player_sum}, My sum: {dealer_sum}") # output the player & the dealer's hand values
    if dealer_sum > player_sum: # if the dealer's sum is greater than the player's sum
        print("I win.") # dealer wins
    elif dealer_sum < player_sum: # vice versa
        print("You win.")
    else: # if they are equal
        print("It's a tie.") # there is a tie
    

# complete the main method
if __name__ == "__main__":
    main()
    
