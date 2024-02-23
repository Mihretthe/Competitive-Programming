for _ in range(int(input())):
    n = int(input())
    reds = list(map(int, input().split()))
    m = int(input())
    blues = list(map(int, input().split()))

    max_value = 0
    r = 0
    b = 0
    currentSum = 0

    while r < n and b < m:
        currentSum += reds[r]
        r += 1
        max_value = max(max_value, currentSum)
        currentSum += blues[b]
        b += 1
        max_value = max(max_value, currentSum)

    while r < n:
        currentSum += reds[r]
        r += 1
        max_value = max(max_value, currentSum)

    while b < m:
        currentSum += blues[b]
        b += 1
        max_value = max(max_value, currentSum)

    max_value = max(max_value, currentSum)
    print(max_value)