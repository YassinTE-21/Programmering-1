import random

# calculating the value of the cards
def hand_value(hand):
    hand_value = 0
    for card in hand:
        value = card.split(" ")[0]
        if value == "King" or value == "Queen" or value == "Jack":
            hand_value += 10
        elif value == "Ace":
            if hand_value < 16:
                hand_value += 11
            elif hand_value < 16:
                hand_value += 1
        else:
            hand_value += int(value)
    return hand_value


# The score of the players
dealer_score = 0
player_score = 0

# Deck of cards
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
values = ["Ace", "King", "Queen", "Jack", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# loop the game until the player wants to quit
play_again = True
while play_again:
    deck = []
    # adding suits and values toghether
    for suit in suits:
        for value in values:
            deck.append(value + " of " + suit)
    random.shuffle(deck)
    hand = []
    dealer_hand = []

    # dealer being able to start with 2 cards
    for i in range(2):
        card = deck.pop()
        dealer_hand.append(card)
    print("The dealer looks at you as he takes two card for himself.")
    print(f"The dealer has {dealer_hand[1]} facing up and another card facing down")
    print("The dealer give you two cards. which are....\n")

    # Dealing the cards for the player
    for i in range(2):
        card = deck.pop()
        hand.append(card)
    print(*hand, sep=", ")
    print(f"The value of your hand is currently {hand_value(hand)}")
    if hand_value(hand) == 21:
        print(
            f"Blackjack! The dealer ended with {hand_value(dealer_hand)} meaning that you won!\n "
        )
        player_score += 1

    # Being able to hit or stand
    while hand_value(hand) < 21:
        hit_or_stand = input("Hit or Stand ? ").lower()
        if hit_or_stand == "hit":
            card = deck.pop()
            hand.append(card)
            print(*hand, sep=", ")
            print(f"The value of your hand is currently {hand_value(hand)}\n")
            # Ending the round if you exceed 21
            if hand_value(hand) > 21:
                print(
                    f"You got {hand_value(hand)} meaning that you exceeded the limit and lost\n"
                )
                dealer_score += 1
                break
            if hand_value(hand) == 21 and hand_value(dealer_hand) < 21:
                print(f"You got ")
        elif hit_or_stand == "stand":
            while hand_value(dealer_hand) < 17:
                for i in range(1):
                    card = deck.pop()
                    dealer_hand.append(card)
                print("The dealer took another card")
            # How the different points are given between the player and the dealer
            if hand_value(hand) == hand_value(dealer_hand):
                print(
                    f"You got {hand_value(hand)} and the dealer got {hand_value(dealer_hand)} meaning it's a draw.\n Dealer wins automaticaly\n "
                )
                dealer_score += 1
                break
            elif (
                hand_value(hand) <= 21
                and hand_value(dealer_hand) <= 21
                and hand_value(hand) > hand_value(dealer_hand)
            ):
                print(
                    f"You got {hand_value(hand)} and the dealer got {hand_value(dealer_hand)} meaning that you won!\n"
                )
                player_score += 1
                break
            elif (
                hand_value(dealer_hand) <= 21
                and hand_value(hand) <= 21
                and hand_value(dealer_hand) > hand_value(hand)
            ):
                print(
                    f"You got {hand_value(hand)} and the dealer got {hand_value(dealer_hand)} meaning that you lost.\n"
                )
                dealer_score += 1
                break
            elif hand_value(dealer_hand) > 21 and hand_value(dealer_hand) > hand_value(
                hand
            ):
                print(
                    f"You got {hand_value(hand)} and dealer got {hand_value(dealer_hand)} meaning that the dealer exceeded the limit and lost\n"
                )
                player_score += 1
                break
    # The command for looping or ending/showing the scores.
    play_again = input("Ready for another round?\n").lower()
    if play_again == "yes":
        continue
    elif play_again == "no":
        play_again = False
        print(f"You ended with {player_score} and the dealer ended with {dealer_score}")

        break

# game loop
