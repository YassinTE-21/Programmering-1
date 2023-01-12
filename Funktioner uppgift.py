# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna


def best(name):
    print(f"{name} är bäst")


best("Yassin")

print(
    "------------------------------------------------------------------------------------"
)


def square(number):
    return number**2


print(square(3))
print(square(7))
print(square(13))
print(square(41))


print(
    "------------------------------------------------------------------------------------"
)


def sums(a, b):
    return a + b


print(sums(3, 8))
print(sums(4, 5))
print(sums(9, 12))
print(sums(12, 32))

print(
    "------------------------------------------------------------------------------------"
)
# Nu blir det lite svårare


def maximum(a, b, c):
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    maximum("4", "7", "19")
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print(
    "------------------------------------------------------------------------------------"
)


def palindrom(ord):
    if ord.lower() == ord[::-1].lower():
        print("Det är en palindrom. ")
    else:
        print("Det är inte en palindrom.")


palindrom("Arda")

print(
    "------------------------------------------------------------------------------------"
)


def prime(nr):
    nr = int(3)
    for i in range(2, nr):
        if (nr % i) == 0:
            print("Det är inte ett prim nummer ")
        break
    else:
        print("Det är ett prim nummer ")
        return nr
