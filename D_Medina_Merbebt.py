from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict


def isOn(num, k):
    number = 1 << k
    return 1 if number & num else 0


def solve():
    n = I()
    a = IL()
    q = I()

    prefix = {}

    # msb = 0
    # for i in a:
    #     msb = max(msb, i.bit_length())

    for i in range(31):
        prefix[i] = [0]
        
        for j in a:
            prefix[i].append(prefix[i][-1] + isOn(j, i))
    
    
    # print(prefix)
    def checker(l, r):
        num = 0
        
        for i in range(31):            
            if (prefix[i][r] - prefix[i][l - 1]) == (r - l + 1):
                num = num | (1 << i)
        
        return num
    
    
    
    answer = []

    for _ in range(q):
        l, k = II()
        if a[l - 1] < k:
            answer.append(-1)
            continue
        r = n + 1
        init = l

        while l + 1 < r: 
            mid = (l + r) // 2

            if checker(init, mid) >= k:
                l = mid 
            else:
                r = mid 

        answer.append(l)
        


    
    print(*answer)

            
    
 
 
 
 
T = I()
for _ in range(T):
    solve()