import random
datorns_score=0
användar_score=0
Möjliga_val=("sten" , "sax" , "påse")

name=input("vad heter du?:" )

#for _ in range(5):
while datorns_score <3 and användar_score<3:  
    Möjliga_val=("sten" , "sax" , "påse")
    Datorns_val=random.choice(Möjliga_val)
    
    Användarval=input("sten, sax eller påse?: ")
    print(f"Du valde {Användarval}. Datorn valde {Datorns_val}")

    if Datorns_val ==  Användarval:
        print("Inga poäng. Lika val. ")

    elif Datorns_val == "sten" and Användarval == "sax": 
        print("1 Poäng till datorn")
        datorns_score=datorns_score+1

    elif Datorns_val == "sten" and Användarval == "påse":
        print(f"1 Poäng till {name}")
        användar_score=användar_score+1

    elif Datorns_val == "sax" and Användarval == "påse":
        print("1 Poäng till Datorn")
        datorns_score=datorns_score+1

    elif Datorns_val == "sax" and Användarval == "sten":
        print(f"1 Poäng till {name}")
        användar_score=användar_score+1

    elif Datorns_val == "påse" and Användarval == "sax":
        print(f"1 Poäng till {name}")
        användar_score=användar_score+1

    elif Datorns_val == "påse" and Användarval == "sten":
        print("1 Poäng till Datorn")
        datorns_score=datorns_score+1
    else:
        print("Du valde något som inte finns.")

print(f"Det slutade med att du hade {användar_score} och datorn slutade med {datorns_score} ")