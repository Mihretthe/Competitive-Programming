from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter
from random import randint

def solve():
    xor = randint(1, 100)
    n = I()
    a = IL()
    a = [i ^ xor for i in a]
    counter = Counter(a)
    not_in = set()

    for i in range(1, n + 1):
        if i ^ xor not in counter:
            not_in.add(i ^ xor)
    answer = []
    till = set()
    for i in range(n):
        num = a[i] 
        if num not in till:
            answer.append(num ^ xor)
            till.add(num)
        else:
            answer.append(not_in.pop() ^ xor)
    
    print(*answer)





 
 
 
 
T = I()
for _ in range(T):
    solve()
