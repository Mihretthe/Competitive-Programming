from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, list(input())))

    subarrays = 0
    previous = defaultdict(int)
    previous[0] = 1
    prefix = 0

    for i in range(n):
        prefix += s[i]
        subarrays += previous[prefix - i - 1]
        previous[prefix - i - 1] += 1
    print(subarrays)