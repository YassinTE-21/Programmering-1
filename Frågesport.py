
score=0
name = input("Hej, vad heter du? ")
frågesport= (input(f"Hej {name}! Är du redo för frågesport?  "))

if frågesport == "ja":
    print("Då kör vi")
else:
    print("Då ses vi någon annan gång. ")



Fråga1=input("Hur många ränder finns på USAs flagga?")

if Fråga1 == "13":
    score=score + 1
    print("Grattis du har rätt! ")

else:
    score=score - 1
    print("Tyvärr hade du fel. USAs flagga har 13 ränder. ")


Fråga2=input("Hur gammal är Hampus Eriksson? ")

if Fråga2 == "28 år" or Fråga2 == "28":
    print("Grattis du har rätt! ")
    score=score + 1
else:
    print("Tyvärr hade du fel. Hampus ålder är 28 år. ")
    score=score - 1

Fråga3=input("Hur många tidszoner finns i Ryssland? ")

if Fråga3 == "11":
    print("Grattis du hade rätt! ")
    score=score + 1

else:
    print("Tyvärr hade du fel. Svaret var 11. ")
    score=score - 1

Fråga4=input("Vad hette den turkiska staden Istanbul fram till 1923?")

if Fråga4 == "Konstantinopel" or Fråga4 == "konstantinopel":
    print("Grattis du har rätt!")
    score= score + 1
else:
    print("Tyvärr hade du fel. Svaret var Konstantinopel.")
    score=score -1

input("Tryck på enter för att se din score")

print(f"du slutade med {score}/4 poäng. ")

    