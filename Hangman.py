import random

words_bank = ['tree', 'book', 'blue', 'train', 'fish', 'woman', 'life', 'freedom', 'iran', 'sky']
cc = []
ic = []
m = 0
#x = random.randint(0, len(words_bank) - 1)
#word = words_bank[x]
word = random.choice(words_bank)
wl = set(word)
print(wl)

while  m < 6:
    for i in range(len(word)):
        if word[i] in cc:
            print(word[i], end = '')
        else:
            print('_', end='')

    print('/n')

    usr_chr = input('Guess :')
    if len(usr_chr) == 1:    
        if usr_chr.upper() in word:
            if usr_chr.upper() in cc:
                print('You already guessed this letter!')
                continue
            else:
                cc.append(usr_chr)
                print('yes')
                if len(cc) == len(wl):
                    print('you win!')
                    break
        else:
            ic.append(usr_chr)
            print('no')
            print('you have ', 6-m, ' guesses left')
            m += 1
            if m == 6:
                print('The man is hanged')
                break
    else:
        print('please enter a single letter please')            

#print(word)