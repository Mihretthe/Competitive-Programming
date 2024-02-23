n = int(input())
a = list(map(int, input().split()))

a.sort()
left = 0
right = n - 1

ans = 0

while left < right:
    ans += (a[left] + a[right]) ** 2
    left += 1
    right -= 1

print(ans)