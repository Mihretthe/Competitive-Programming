from collections import Counter
import random

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ran = int(random.randint(1,100))
    a = list(map(lambda x : x ^ ran, a))
    # a.sort()

    l = 0
    r = 0

    ans = []

    counter = Counter(a)

    if max(counter.values()) < k:
        print(-1)
        continue

    suitable = []
    for key, value in counter.items():
        if value >= k:
            suitable.append(key^ran)
    suitable.sort()

    for i in range(1, len(suitable)):
        if suitable[i] == suitable[i - 1]  + 1:
            r = i
            if ans:
                if ans[1] - ans[0] < suitable[r] - suitable[l]:
                    ans = [suitable[l] ,suitable[r] ]
            else:
                ans = [suitable[l] ,suitable[r]]
        else:
            l = i

    if not ans:
        ans = [suitable[0] ,suitable[0] ]

    print(*ans)