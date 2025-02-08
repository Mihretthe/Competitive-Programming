from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, f, k = II()
    array = IL()
    num = array[f - 1]

    array.sort(reverse = True)

    first = set(array[:k])
    second = set(array[k:])

    if num in first and num in second:
        print("MAYBE")
    elif num in second:
        print("NO")
    else:
        print("YES")


 
 
 
 
T = I()
for _ in range(T):
    solve()