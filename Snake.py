n = int(input('How long do you want your snake to be?! '))

for i in range(3,n + 3):
    if i%2 == 1:
        print('*', end = '')
    else:
        print('#', end = '')