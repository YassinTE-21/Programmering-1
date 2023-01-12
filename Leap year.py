def Leap(year):
    if year % 4 == 0:
        print("Det är ett skottår ")
    else:
        print("Det är inte ett skottår ")


while True:
    year = int(input("Skriv ett år: "))
    Leap(year)
