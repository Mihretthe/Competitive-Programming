def sumd(num):
    ans = 0
    while num > 0:
        ans += num % 10
        num //= 10
    return ans

for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += sumd(i)
    print(ans)

    


