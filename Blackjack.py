import random
def hand_value(hand):
    hand_value = 0
    for card in hand:
        value = card.split(" ")[0]
        if value == "King" or value == "Queen" or value == "Jack":
            hand_value += 10
        elif value == "Ace":
            hand_value += 11
        else:
            hand_value += int(value)
    return hand_value

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
values = ["Ace", "King", "Queen", "Jack", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

deck = []
for suit in suits:
     for value in values:
          deck.append(value + " of " + suit )

random.shuffle(deck)
hand=[]

for i in range(2):
    card=deck.pop()
    hand.append(card)
print(*hand, sep=", ")
print(f"The value of your hand is currently {hand_value(hand)}")

while (hand_value(hand)) <=21:
    hit=input("Another card? (Y/N) ").capitalize
    if hit == "y":
        hand.append(card)
    print(f"The value of your hand is currently {hand_value(hand)}")
    


