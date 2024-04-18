def solve():
    for _ in range(int(input())):
        n = int(input())
        #sinp = input()
        n, k = map(int,input().split())
        a = list(map(int,input().split()))
        t = list(map(int,input().split()))
        ans = []
        
        for i in range(n):
            res = (abs(i-a[i])+t[i])+1
            re = abs(i-a[i]+t[i]) +1

            ans.append(res,re)

            

    
t = int(input())
while t:
    solve()
    t-=1