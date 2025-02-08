from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    s = set(S())
    if  len(s) % 2:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")
    
 
 
 
 
T = 1
for _ in range(T):
    solve()