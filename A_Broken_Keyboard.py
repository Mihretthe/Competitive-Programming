def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from collections import Counter
 
def solve():
    s = input()

    ans = s[:]
    
    for i in s:
        ans = ans.replace(i*2, "_")
    
    ans = ans.replace("_", "")
    ans = "".join(sorted(set(ans)))
    print(ans)
    
 
 
T = I()
for _ in range(T):
    solve()