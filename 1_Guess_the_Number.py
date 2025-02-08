from sys import stdin, stdout

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    left = 1
    right = 1000000

    while left <= right:
        mid = (left + right) // 2
        print(mid)
        stdout.flush()
        inp = input()

        if inp == ">=":
            left = mid + 1
        else:
            right = mid - 1
    print("! ", right)
    stdout.flush()
    exit()
 
 
 
 
T = 1
for _ in range(T):
    solve()