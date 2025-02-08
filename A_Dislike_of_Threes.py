from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

collect = []

for i in range(1, 1667):
    if i % 3 == 0 or i % 10 == 3:
        continue
    collect.append(i)

# print(len(collect))
    

def solve():
    k = I()
    print(collect[k - 1])
 
 
 
 
T = I()
for _ in range(T):
    solve()