#Greatest Common Divisor
import math

n = int(input('How many numbers do you want to enter?! '))
a = []
for i in range(n):
    x = int(input('Enter: '))
    a.append(x)

gcd = math.gcd(*a)
print(gcd)