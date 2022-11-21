a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))

if a < b:
    s = a
else: 
    s = b

for i in range(1,s + 1):
    if a%i == 0 and b%i == 0:
        gcd = i

print('GCD of the two numbers is ,', gcd)
