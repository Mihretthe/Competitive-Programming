n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
count = 0
j = 0
for i in range(n):
    if i > 0 and a[i] == a[i - 1]:
        ans += count
    else:
        count = 0
        while j < m:
            if a[i] == b[j]:
                count += 1
            elif b[j] > a[i]:
                break
            j += 1       
        ans += count

print(ans)