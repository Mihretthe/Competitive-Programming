from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def fileName(string):
    string = string.split()
    string[0] = string[0][:-1]
    
    print("_".join(string))
    
fileName("C. Penalty Shootout")


def solve():
    n, x = II()
    count = 0
    for _ in range(n):
        operation, d = SL()
        d = int(d)
        
        if operation == "+":
            x += d
        else:
            if x >= d:
                x -= d
            else:
                count += 1
    print(x, count)
 
 
 
 
T = 1
for _ in range(T):
    solve()