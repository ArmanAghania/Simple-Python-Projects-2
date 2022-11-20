import math

n = int(input('How many numbers do you want to enter?! '))
a = []
for i in range(n):
    x = int(input('Enter: '))
    a.append(x)

lcm = math.lcm(*a)
print(lcm)