from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    n, q = II()
    a = IL()
    k = IL()

    betweens = []

    for i in range(n):
        for j in range(i + 1, n):
            betweens.append([a[i], a[j]])
    
    answer = defaultdict(int)
    for i in k:
        count = 0
        for s, e in betweens:
            if s <= i <= e:
                count += 1
        answer[count] += 1


    ans = []

    for i in k:
        ans.append(answer[i])
    
    print(*ans)
 
 
T = I()
for _ in range(T):
    solve()