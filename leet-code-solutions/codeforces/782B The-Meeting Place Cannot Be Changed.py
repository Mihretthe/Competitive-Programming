n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

zip_x = list(zip(x,v))
zip_x.sort()

def validate(mid):
    mini = 0
    maxi = float('inf')
    for x, v in zip_x:
        mini = max(mini, x - (mid * v))
        maxi = min(maxi, x + (mid * v))

    return mini <= maxi

left = 0
right = max(x)

while right - left > 1e-7:
    mid = (left + right) / 2
    if validate(mid):
        right = mid
    else:
        left = mid

print(right)