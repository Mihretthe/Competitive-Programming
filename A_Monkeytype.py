from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    alpha = S()
    s = S()
    array = []

    for i in s:
        array.append(alpha.index(i))
    
    answer = 0

    for i in range(1, len(s)):
        answer += abs(array[i] - array[i - 1])
    
    print(answer)


 
 
 
 
T = I()
for _ in range(T):
    solve()