def solve():
    
    n = int(input())
    s = input()
    #a = list(map(int,input().split()))
    nums = []
    operations = []
    k = 0
    for i in range(n):
        
        if s[i] == "L":
            if i < n // 2:
                operations.append((i,n - 1 - i))
            nums.append(i)
        else:
            if i >= n // 2:
                operations.append((i,i))
            nums.append(n - i - 1)
 
   

    operations.sort(key = lambda x: x[1])

    total = sum(nums)
    ans = []
    for i in range(n):
        if operations:
            i, num = operations.pop()
            total += (num - nums[i])
        
        ans.append(total)

    print(*ans)

    
t = int(input())
while t:
    solve()
    t-=1