l = []

n = int(input('Number of Elements? '))

for i in range(n):
    e = int(input())

    l.append(e)
print(l)
if l == sorted(l):
    print('it is sorted')
else:
    print('it is not sorted')