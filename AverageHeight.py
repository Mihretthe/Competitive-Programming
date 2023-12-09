for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(key = lambda x : x % 2 == 0)
    print(*nums)
