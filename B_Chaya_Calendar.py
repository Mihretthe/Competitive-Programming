for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n % 2 == 0:
        print(2 * a[-1])
    else:
        print(n * a[0])