from math import sqrt

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a = sum(a)

    if sqrt(a).is_integer():
        print("YES")
    else:
        print("NO")