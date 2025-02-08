from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    letters = "abcdefghijklmnopqrstuvwxyz"
    s = S()
    indices = defaultdict(list)
    length = len(s)

    for i in range(length):
        indices[s[i]].append(i + 1)
    
    a = s[0]
    b = s[-1]
    index_a = letters.index(a)
    index_b = letters.index(b)
    answer = []
    if a <= b:
        for i in range(index_a, index_b + 1):
            letter = letters[i]
            if letter <= b:
                answer.extend(indices[letter])
    else:
        for i in range(index_a, index_b - 1, -1):
            letter = letters[i]
            if letter <= a:
                answer.extend(indices[letter])

    print(abs(letters.index(a) - letters.index(b)), len(answer))
    print(*answer)
    
    

 
T = I()
for _ in range(T):
    solve()