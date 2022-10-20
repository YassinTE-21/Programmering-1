import random
gissningar=0

Ord=("Dator", "Flaska", "Mobil", "Låda", "Flygplan" )
Guess=input(Ord)

while gissningar<5:
    datorns_val=random.choice(Ord)
    len(datorns_val)
    Word=len(datorns_val)*"_"
    input(Word)
    if Guess == datorns_val:
        pass
    else:
        break

        