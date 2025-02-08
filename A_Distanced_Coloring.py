testcases = int(input())
for _ in range(testcases):
    n, m, k = map(int, input().split())
    print(min(n, k) * min(m, k))