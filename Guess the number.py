import random

num = random.randint(1, 10)
guess =()

while guess != num:
    guess = input("Gissa ett tal mellan 1 och 10: ")
    guess = int(guess)

    if guess == num:
        print("Du hade rätt!")
        break
    else:
        print("Tyvärr hade du fel. Testa igen.\n ")