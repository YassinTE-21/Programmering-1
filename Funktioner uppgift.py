# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna


def best(name):
    name="Yassin"
    print(f"{name} är bäst" ) 
best("Yassin")

print("------------------------------------------------------------------------------------")

def square(number):
    # TODO Returnera talet kvadrerat
    # Ex: 5 in - 25 ut
    pass
    return number**2
print(square(3))
print(square(7))
print(square(13))
print(square(41))


print("------------------------------------------------------------------------------------")

def sums(a, b):
    # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
    return a+b
print(sums(3,8))
print(sums(4,5))
print(sums(9,12))
print(sums(12,32))

print("------------------------------------------------------------------------------------")
# Nu blir det lite svårare


def maximum(a, b, c):
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    maximum("4","7","19")
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
    

def palindrom(ord):
    # TODO Returnera True om ord är ett palindrom
    # Ex: abba in - True ut
    # Palindrom är ett ord som stavas likadant baklänges och framlänges.
    pass


def prime(nr):
    nr=int(3)
    for i in range (2, nr):
        if (nr % i) == 0:
            print("Det är inte ett prim nummer ")
        break
    else:
        print("Det är ett prim nummer ")
    return nr 
print(prime(5))          
