from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

prefix = [0]

from bisect import bisect_right

for i in range(1, 1000001):
    prefix.append(prefix[-1] + i)


def solve():
    n = I()
    alice = 1
    bob = 0
    index = bisect_right(prefix, n)
    turn = False
    n -= 1

    for i in range(2, index, 2):
        if turn:
            if n - (i + 1 + i) > 0:
                alice += (i + 1 + i)
                turn = False
                n -= (i + 1 + i)
            else:
                alice += n
                n = 0
                break
        else:
            if n - (i + 1 + i) > 0:

                bob += (i + i + 1)
                turn  = True
                n -= (i + 1 + i)
            else:
                bob += n
                n = 0
                break
    if n and turn:
        alice += n
    elif n and not turn:
        bob += n
    print(alice, bob)




    


 
 
 
T = I()
for _ in range(T):
    solve()