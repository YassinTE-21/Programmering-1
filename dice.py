import random
min = 1
max = 6

rulla_igen = "yes"

while rulla_igen == "yes" or rulla_igen == "y":
    print ("Rullar...")
    print (random.randint(min, max))
    rulla_igen = (input("Rulla igen?"))