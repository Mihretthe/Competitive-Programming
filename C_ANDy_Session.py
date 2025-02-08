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
    return bool(number & num)


def solve():
    n, k = II()
    a = IL()

    counter = defaultdict(int)

    andy = a[0]

    for i in a:
        andy &= i

    for i in a:
        for j in range(33):
            counter[j] += 1 - isOn(i, j)

    answer = ["0"] * 33

    for i in range(33, -1, -1):
        if isOn(andy, i):
            answer[i] = "1"
        elif i <= 30 and counter[i] <= k:
            k -= counter[i]
            answer[i] = "1"
        
        
    
    print(max(andy, int("".join(answer)[::-1], 2)))



    
   
    
    
    

                                                                                                                                                                                   
        

 
 
 
 
T = I()
for _ in range(T):
    solve()