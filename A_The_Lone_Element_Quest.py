from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    counter = Counter(a)
    for i in counter:
        if counter[i] == 1:
            print(a.index(i) + 1)
