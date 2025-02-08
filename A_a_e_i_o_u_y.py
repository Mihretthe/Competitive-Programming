from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    s = S()

    answer = []
    vowels = "aeiouy"


    for i in s:
        if answer and answer[-1] in vowels and i in vowels:
            continue
        answer.append(i)
    
    print("".join(answer))


 
 
 
 
T = 1
for _ in range(T):
    solve()