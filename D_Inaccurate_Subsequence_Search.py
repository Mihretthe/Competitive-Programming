from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter, defaultdict
from random import randint

def check(counter, current):
    count = 0
    for i in current:
        count += min(counter[i], current[i])
    return count 



def solve():
    n, m, k = II()
    a = IL()
    b = IL()
    
    random = randint(1, 100)
    a = list(map(lambda x : x ^ random, a))
    b = list(map(lambda x : x ^ random, b))

    counter = Counter(b)
    count = 0
    current = defaultdict(int)

    for i in range(m):
        if a[i] in counter:
            current[a[i]] += 1

    init = check(counter,current)
    if init >= k:
        count += 1
    
    for i in range(1, n - m + 1):
        if a[i + m - 1] in counter:
            current[a[i + m - 1]] += 1
            if counter[a[i + m - 1]] >= current[a[i + m - 1]]:
                init += 1

        if a[i - 1] in counter:
            current[a[i - 1]] -= 1
            if counter[a[i - 1]] > current[a[i - 1]]:
                init -= 1
 
        if init >= k:
            count += 1
    print(count)
    


    
 
 
 
 
T = I()
for _ in range(T):
    solve()