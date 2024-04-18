
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
from collections import defaultdict




def solve():
    length = I()
    s = input()

    def check(mid):
        every = []

        for i in range(0,length):            
            every.append(s[i:i + mid])
        
        for string in every:
            string = string * (length // mid)
            if len(string) != length:
                continue
            count = 0
            for i in range(length):
                if string[i] != s[i]:
                    count += 1
                if count > 1:
                    break
            else:
                return True
        

    left = 0
    right = length 
    ans = length

    while left + 1 < right:
        mid = (left + right) // 2
        
        if check(mid):
            right = mid 
            ans = min(ans, mid)
        else:
            left = mid 
        
    print(ans)






    

    
    
    
    
T = I()
for _ in range(T):   
    solve()
    