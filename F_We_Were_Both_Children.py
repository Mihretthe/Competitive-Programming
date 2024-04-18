from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)  # Count the frequency of each number

    max_count = 0

    for i in range(1, n + 1):
        count = 0
        for num in freq:
            if i % num == 0:
                count += freq[num]  # Count the multiples of num
        max_count = max(max_count, count)

    print(max_count)