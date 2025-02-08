from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = IL()

    index = 0
    answer = 0

    while index < n:
        parity = a[index] % 2
        count = 0
        while index < n:
            if a[index] % 2 == parity:
                count += 1
                index += 1
            else:
                break
        else:
            index += 1
        answer += count - 1
    
    print(answer)

    
 
 
 
T = I()
for _ in range(T):
    solve()