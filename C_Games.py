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

    evens = []
    odds = []

    

    for i in a:
        if i % 2:
            odds.append(i)
        else:
            evens.append(i)
    odds.sort()
    evens.sort()

    turn = True
    alice = []
    bob = []

    while evens and odds:
        if turn:
            if odds[-1] > evens[-1]:
                odds.pop()
            else:
                alice.append(evens.pop())
            turn = False            
        else:
            if evens[-1] > odds[-1]:
                evens.pop()
            else:
                bob.append(odds.pop())
            turn = True
    
    if evens:
        if not turn:
            evens.pop()
        while evens:
            alice.append(evens.pop())
            if evens:
                evens.pop()
    if odds:
        if turn:
            odds.pop()
        while odds:
            bob.append(odds.pop())
            if odds:
                odds.pop()
    
    alice = sum(alice)
    bob = sum(bob)

    if alice == bob:
        print("Tie")
    elif alice > bob:
        print("Alice")
    else:
        print("Bob")
 
 
 
 
T = I()
for _ in range(T):
    solve()