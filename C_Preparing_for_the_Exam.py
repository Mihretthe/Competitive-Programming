from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from random import randint

def solve():
    xor = randint(1, 100)
    n, m, k = II()
    a = IL()
    q = IL()
    a = [i ^ xor for i in a]
    q = set([i ^ xor for i in q])
    
    

    # if n - k > 1:
    #     print("".join(["0"] * m))
    #     return
    
    answer = []
    
    qnot = set()

    for i in range(1, n + 1):
        if i ^ xor not in q:
            qnot.add(i ^ xor)
    
    if len(qnot) > 1:
        print("".join(["0"] * m))
        return
    if len(qnot) == 0:
        print("".join(["1"] * m))
        return

    for i in a:
        if i in qnot:
            answer.append("1")
        else:
            answer.append("0")
    
    print("".join(answer))


    
    

    
    
    
    


    

    
 
 
 
T = I()
for _ in range(T):
    solve()