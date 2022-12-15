def Leap(Year):
    if Year % 4 == 0:
        print("Det är ett skottår ")
    else:
        print("Det är inte ett skottår ")


while True:
    Year = int(input("Skriv ett år: "))
    Leap(Year)
