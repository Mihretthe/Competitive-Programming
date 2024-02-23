n, s = map(int, input().split())
a = list(map(int, input().split()))
max_segment = 0

add = 0
starter = 0
for i in range(n):
    if add > s:
        add = 0
        max_segment = max(max_segment,i - 1 - starter)
        starter = i
    elif add == s:
        add = 0
        max_segment = max(max_segment,i - starter)
        starter = i + 1

    add += a[i]

print(max_segment)