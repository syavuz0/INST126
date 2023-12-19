# Blackjack Consolidation Assignment 

import random

# assigning variables  
card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in card_categories for card in cards_list]

# returns the values of the highest cards, the rest fall between [2-10]
def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])

# displaying the cards and score of the player 
def display_cards_and_score(cards, score, player_type):
    print(f"Cards {player_type} Has: {cards}")
    print(f"Score Of The {player_type}: {score}\n")

# takes score of the player and dealer and returns a string that tells you the winner
# or if a tie occured between the both 
def determine_winner(player_score, dealer_score):
    if player_score > 21 or (dealer_score <= 21 and dealer_score > player_score):
        return "Dealer"
    elif dealer_score > 21 or player_score > dealer_score:
        return "Player"
    else:
        return "Tie"

# shuffles the deck and removes the last two cards from the deck
# while assigning it to the player_cards and dealer_cards
random.shuffle(deck)
player_cards = [deck.pop(), deck.pop()]
dealer_cards = [deck.pop(), deck.pop()]

while True:
    # calculates the total score of the player's hand using the card_value function
    player_score = sum(card_value(card) for card in player_cards)
    dealer_score = sum(card_value(card) for card in dealer_cards)

    display_cards_and_score(player_cards, player_score, "Player")

    choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower()
    
    # if player chooses to continue, a new card is 'popped' from the deck, represents player requesting another card 
    # if they choose stop, the loop is broken with "break"
    # the loop automatically continues if an answer is provided that does not fall under play or stop
    if choice == "play":
        player_cards.append(deck.pop())
    elif choice == "stop":
        break
    else:
        print("Invalid choice. Please try again.")
        continue
    # if the score exceeds 21 it indicates a bust and breaks the loop 
    if player_score > 21:
        display_cards_and_score(dealer_cards, dealer_score, "Dealer")
        print("Dealer wins (Player Loss Because Player Score is exceeding 21)")
        break

# i've researched a bit, and as long as a dealers score is less than 17 the loop continues 
while dealer_score < 17:
    dealer_cards.append(deck.pop())
    dealer_score += card_value(dealer_cards[-1]) # updates the dealers total score by adding the draw of the last card

# displays the dealers hand and score
display_cards_and_score(dealer_cards, dealer_score, "Dealer")

# determines the winner or if there's a tie 
winner = determine_winner(player_score, dealer_score)

# prints the results 
print(f"{winner} wins!" if winner != "Tie" else "It's a tie.")
