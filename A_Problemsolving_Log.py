from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = input()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0

    counter = Counter(s)
    for key, value in counter.items():
        if value >= (letters.index(key) + 1):
            count += 1

    print(count)


