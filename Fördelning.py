#A= hur många specifika saker vi har
#B=hur många personer

A = ""
while A != "stop":
    A=int (input("Hur många saker har du? "))
    B=int (input("Hur många personer vill du dela det med? "))

    print(f"Hur många saker får varje person?",{A//B})
    print(f"Hur många blir över?",{A%B})

