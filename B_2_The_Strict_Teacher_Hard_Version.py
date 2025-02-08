from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_left, bisect_right

def solve():
    n, m, q = II()
    teachers = IL()

    teachers.sort()
    a = IL()
    for i in a:
        b = i
        index = bisect_left(teachers, b)
        if index == 0:
            print(teachers[0] - 1)
        elif index == m:
            print(n - teachers[-1])
        else:
            print((teachers[index] - teachers[index - 1]) // 2)

    
 
 
 
 
T = I()
for _ in range(T):
    solve()