n = int(input())
t = list(map(int, input().split()))

t.sort()
prefix = [0]
count = 0

for i in range(n):
    prefix.append(prefix[-1] + t[i])

for i in range(n):
    if t[i] >= prefix[i]:
        count += 1

print(count)