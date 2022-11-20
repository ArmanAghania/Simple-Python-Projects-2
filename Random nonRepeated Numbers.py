import random

n = int(input('how many numbers do you want?! (Please enter and integer)'))

a = []
while len(a) < n:
    x = random.randint(1,100)
    if x not in a:
        a.append(x)
    else:
        continue

print(a)