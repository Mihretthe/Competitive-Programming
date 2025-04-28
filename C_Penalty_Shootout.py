from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def doIt(s, a):
    if a:
        first = 0
        second = 0
        for i in range(10):
            if i % 2:
                if s[i] != "0":
                    second += 1
                remain = 5 - ceil(i / 2)
                if first + remain < second:
                    return i + 1
                if second + remain< first:
                    return i + 1 
                               
            else:
                if s[i] == "1":
                    first += 1
                remain = 5 - ceil(i / 2)
                if second + remain < first:
                    return i + 1
                if first + remain - 1 < second:
                    return i + 1 
        return 10
        
    else:
        first = 0
        second = 0
        for i in range(10):
            if i % 2:
                if s[i] == "1":
                    second += 1
                remain = 5 - ceil(i / 2)
                if first + remain < second:
                    return i + 1
                if second + remain< first:
                    return i + 1 
                
            else:
                if s[i] != "0":
                    first += 1
                remain = 5 - ceil(i / 2)
                if second + remain < first:
                    return i + 1
                if first + remain - 1 < second:
                    return i + 1 
        
        return 10



def solve():
    s = S()
    print(min(doIt(s, 1), (doIt(s, 0))))
    
    
 
 
 
T = I()
for _ in range(T):
    solve()