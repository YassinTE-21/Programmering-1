from random import random


gissningar=0

Ord=("Dator", "Flaska", "Mobil", "Låda", "Flygplan", )

while gissningar<5:
    Ord_att_gissa=("Dator", "Flaska", "Mobil", "Låda", "Flygplan", )
    datorn_val=random.choice(Ord_att_gissa)
