from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import deque

def solve():
    n = I()
    ax, ay = II()
    ax -= 1
    ay -= 1
    bx, by = II()
    bx -= 1
    by -= 1
    grid = []

    for _ in range(n):
        row = list(S())
        grid.append(row)
    
    directions = [(1, 1),(-1,-1), (-1, 1), (1, -1)]

    deck = deque([(ax, ay, 1, None, None)])

    def inbound(row, col):
        return row >= 0 and row < n and col >= 0 and col < n

    visited = set([(ax, ay, True), (ax, ay, False)])

    if ax == bx and ay == by:
        print(0)
        return
    while deck:
        # print(deck)
        row, col, level, prer, prec = deck.popleft()
        if row == bx and col == by:
            print(level)
            break

        for i in range(4):
            r, c = directions[i]
            newr = r + row
            newc = c + col

            if inbound(newr, newc) and (newr, newc, i < 2) not in visited and grid[newr][newc] == ".":
                if prer == prec == None or ((prer - row) == (row - newr) and (prec - col) == (col - newc)):
                    deck.append((newr, newc, level, row, col))
                else: 
                    deck.append((newr, newc, level + 1, row, col))
                
                visited.add((newr, newc, i < 2))
 


    else:
        print(-1)

 
T = 1
for _ in range(T):
    solve()