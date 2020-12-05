import random
import time

ls = ['a', 116, 'e', 94, 'i', 86, 'r', 68, 'n', 68, 'l', 60, 'k', 47, 'd', 46, 'ı', 38, 'o', 36, 'm', 34, 'u', 34, 't', 33, 's', 33,
      'b', 28, 'y', 27, 'ü', 18, 'v', 17, 'ş', 16, 'g', 15, 'z', 14, 'ç', 13, 'h', 13, 'c', 11, 'ğ', 9, 'p', 8, 'ö', 7, 'f', 5, 'j', 2]
bag = []
count = 0
size = 6
for i in range(len(ls) // 2):
    for j in range(ls[count + 1]):
        bag.append(ls[count])
    count += 2
print('  ', end='')
for i in range(size):
    print(i + 1, end=' ')
print()
for i in range(size):
    print(i + 1, end=' ')
    for j in range(size):
        rand = random.randrange(len(bag))
        print(bag[rand], end=' ')
    print()
