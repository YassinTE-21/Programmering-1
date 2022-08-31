Seconds=()
Age = ()
username=()

print(username)
print(Age)

username = input("Hej, vad heter du? ")
Age=int (input(f"Hej {username}! Hur gammal är du? "))

#seconds=Age * (365*24*60*60)
print(f"Då betyder det att din ålder i sekunder är:{Age*31556926}")
print(f"Då betyder det att din ålder i minuter är:{Age*525949}")
print(f"Då betyder det att din ålder i timmar är:{Age*8766}")
print(f"Då betyder det att din ålder i dagar är:{Age*365}")
print(f"Då betyder det att din ålder i månader är:{Age*12}")