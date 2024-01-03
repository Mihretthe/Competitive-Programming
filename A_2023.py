from math import prod

for _ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    
    if 2023 % prod(b) == 0:
        print("YES")
        ans = [1] * (k - 1)
        print(2023 // prod(b), *ans)
    else:
        print("NO")