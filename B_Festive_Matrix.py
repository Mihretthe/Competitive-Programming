n = int(input())
ans = 0

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if i - j == 0:
            ans += row[j]
        elif i + j == n - 1:
            ans += row[j]
        elif j == n //2:
            ans += row[j]
        elif i == n//2:
            ans += row[j]

print(ans)


