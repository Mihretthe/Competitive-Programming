from collections import Counter

for _ in range(int(input())):
    n = int(input())
    

    word = []

    for _ in range(n):
        word.append(input())

    word = "".join(word)

    counter = Counter(word)

    for key, value in counter.items():
        if value % n != 0:
            print("NO")
            break
    else:
        print("YES")