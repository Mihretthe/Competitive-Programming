n = int(input())
a = list(map(int, input().split()))

a.sort()

first = a[:n//2]
last = a[n//2:]

print(sum(first)**2 + sum(last)**2)