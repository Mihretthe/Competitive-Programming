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
    negative = []
    positive = []
    zeros = []

    for num in a:
        if num < 0:
            negative.append(num)
        elif num > 0:
            positive.append(num)
        else:
            zeros.append(num)
    
    if len(negative) % 2 == 0:
        zeros.append(negative.pop())

    if len(positive) == 0:
        positive.append(negative.pop())
        positive.append(negative.pop())

    print(len(negative), *negative)
    print(len(positive), *positive)
    print(len(zeros), *zeros)

 
 
 
 
T = 1
for _ in range(T):
    solve()