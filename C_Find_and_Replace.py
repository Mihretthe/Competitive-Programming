
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
from collections import defaultdict
    

def solve():
    n = I()
    s = input()
    hashmap = defaultdict(int)
    binary = []

    for i in s:
        if not hashmap:
            hashmap[i] = "0"
        if i not in hashmap:
            if binary[-1] == "0":
                hashmap[i] = "1"
            else:
                hashmap[i] = "0"
            
            
        binary.append(hashmap[i])
    binary = "".join(binary)
    if "00" in binary or "11" in binary:
        print("NO")
    else:
        print("YES")


    

    
    
    
T = I()
for _ in range(T):   
    solve()
    

