n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

i = 0
j = 0
a.sort()
b.sort()
count = 0

while i < n and j < m:
    if a[i] == b[j] or a[i] - 1 == b[j] or a[i] + 1 == b[j]:
        count += 1
        i += 1
        j += 1
    else:
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
print(count)
