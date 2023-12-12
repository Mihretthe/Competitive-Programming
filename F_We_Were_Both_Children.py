t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
   
   
    ans = 0
    count = 0

    for i in range(1,n + 1):
        count = 0
        for j in range(n):
            if i % a[j] == 0:
                count += 1

        ans = max(ans, count)
    
    ans = max(ans, count)
    print(ans) 