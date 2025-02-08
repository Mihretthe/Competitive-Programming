from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    n = I()
    points = []
    points_set = set()
    for _ in range(n):
        x, y = II()
        points.append((x, y))
        points_set.add((x, y))
    count = 0
    for i in range(n):
        x, y = points[i]
        for j in range(i + 1, n):
            x1, y1 = points[j]
            if (x + x1) % 2 == 0 and (y + y1) % 2 == 0:
                if ((x + x1) // 2, (y + y1) //2) in points_set:
                    count += 1
    print(count)


 
T = 1
for _ in range(T):
    solve()