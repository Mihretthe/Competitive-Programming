from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter





def solve():
    n = I()
    a = IL()
    
    
    calculated = set()
    def calc(num):
        count = 0
        calculated.add(num)
        while num % 2 == 0:
            num //= 2
            calculated.add(num)
            count += 1
            
        return count
    
    a = [i for i in a if i % 2 == 0]
    a.sort(reverse=True)
    
    counter = Counter(a)
    
    count = 0
    
    for key, value in counter.items():
        if key not in calculated:
            count += (calc(key))
    
    print(count)
 
 
 
T = I()
for _ in range(T):
    solve()