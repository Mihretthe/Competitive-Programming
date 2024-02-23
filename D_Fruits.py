from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

hashmap = defaultdict(int)
a.sort()

sorted_a = a[::-1]

for _ in range(m):
    hashmap[input()] += 1

values = list(hashmap.values())

values.sort(reverse = True)

mini = 0
maxi = 0

for i in range(len(values)):
    mini += (sorted_a[i] * values[i])
    maxi += (a[i] * values[i])

print(maxi, mini)