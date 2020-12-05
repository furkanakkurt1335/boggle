import random
f = open('sevenLettered-oneWord-List.txt', encoding='utf-8')
txt = f.read()
lst = txt.split()
randNum = random.randrange(len(lst))
word = lst[randNum]


# board generation
ls = ['a', 116, 'e', 94, 'i', 86, 'r', 68, 'n', 68, 'l', 60, 'k', 47, 'd', 46, 'ı', 38, 'o', 36, 'm', 34, 'u', 34, 't', 33, 's', 33,
      'b', 28, 'y', 27, 'ü', 18, 'v', 17, 'ş', 16, 'g', 15, 'z', 14, 'ç', 13, 'h', 13, 'c', 11, 'ğ', 9, 'p', 8, 'ö', 7, 'f', 5, 'j', 2]
bag = []
board = []
count = 0
size = 6

row = []
for i in range(size):
    row.append(' ')
for i in range(size):
    board.append(row.copy())

# choose board place of word and place it
r1 = random.randrange(size)
r2 = random.randrange(size)
ways = {0: 'r', 1: 'l', 2: 'u', 3: 'd'}
board[r1][r2] = word[:1]
w = word[1:]
for i in w:
    while(True):
        way = random.randrange(4)
        way = ways[way]
        fr1 = r1
        fr2 = r2
        if way == 'r' and r2 != size - 1:
            r2 += 1
        elif way == 'l' and r2 != 0:
            r2 -= 1
        elif way == 'u' and r1 != 0:
            r1 -= 1
        elif way == 'd' and r1 != size - 1:
            r1 += 1
        else:
            continue
        if board[r1][r2] == ' ':
            board[r1][r2] = i
            break
        else:
            r1 = fr1
            r2 = fr2

count = 0
for i in range(len(ls) // 2):
    for j in range(ls[count + 1]):
        bag.append(ls[count])
    count += 2

for i in range(size):
    for j in range(size):
        if board[i][j] == ' ':
            n = bag[random.randrange(len(bag))]
            board[i][j] = n
            # print board
for i in range(size):
    print(i + 1, end=' ')
    for j in range(size):
        print(board[i][j], end=' ')
    print()
input()
print(word)

"""
extract 7 lettered words from list
f = open('tdkA.txt')
txt = f.read()
lst = txt.split()
sevenList = []
for i in lst:
    if len(i) == 7 and i.startswith('a'):
        sevenList.append(i)
w = open('out.txt', 'w')
for i in sevenList:
    w.write(i)
    w.write(' ')
"""
