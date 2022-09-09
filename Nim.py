from ast import While
P=int(input("Hur många pinnar vill du köra med? "))

name_1=input("Vad är den första spelarens namn?: " )

name_2=input("Vad är den andra spelarens namn?: ")

print(f"Då är det {name_1} mot {name_2}.  ")

while P >0: 
    print(f"Det är {name_1}s tur. ")
    
    ta_bort = int(input(f"Det finns {P} sticks. Mellan 1,2,3 hur många vill du ta? "))
    P-=ta_bort

    print(f"Det är {name_2}s tur. ")

    ta_bort = int(input(f"Det finns {P} sticks. Mellan 1,2,3 hur många vill du ta? "))
    P-=ta_bort