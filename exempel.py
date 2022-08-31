import random
min = 1
max = 6
res = {1:0,2:0,3:0,4:0,5:0,6:0}

for _ in range(1000):
    
    res[random.randint(min, max)] += 1


print(res)