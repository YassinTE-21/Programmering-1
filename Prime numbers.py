from asyncore import loop

num=int(input("vilket nummer vill du kolla? "))

for i in range (2, num):
    if (num % i) == 0:
        print("Det är inte ett prim nummer ")
        break
else:
    print("Det är ett prim nummer ")
            
