from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    numbers = []

    for _ in range(n):
        numbers.append(S())

    length = len(numbers[0])
    ans = 0

    for j in range(length):
        digit = numbers[0][j]
        count = 0
        for i in range(n):
            if numbers[i][j] == digit:
                count += 1
        if count == n:
            ans += 1
        else:
            break
    
    print(ans)



 
 
 
 
T = 1
for _ in range(T):
    solve()