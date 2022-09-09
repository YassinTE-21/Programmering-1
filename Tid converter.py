
for _ in range(20):
    nummer=int(input("lägg till nummer: "))
    timme=nummer//3600
    timme1=nummer%3600
    minut=timme1//60
    sekund=timme1%60

    print(timme,"timmar",minut,"minuter",sekund,"sekunder") 
