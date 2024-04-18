
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from collections import deque



def solve():
    n, m, x = II()
    
    deck = deque([x])


    for _ in range(m):
        r, c = list(input().split())
        r = int(r)
        if c == "?":
            for j in range(len(deck)):
                i = deck.popleft()
                
                if ((i + r) % n) == 0:
                    deck.append(n)
                else:
                    deck.append((i + r) % (n))
                
                if ((i - r) % n) == 0:
                    deck.append(n)
                else:
                    deck.append((i - r) % (n))

        elif c == "0":
            for j in range(len(deck)):
                i = deck.popleft()
                if ((i + r) % n) == 0:
                    deck.append(n)
                else:
                    deck.append((i + r) % (n))
        elif c == "1":
            for j in range(len(deck)):
                i = deck.popleft()
                if ((i - r) % n) == 0:
                    deck.append(n)
                else:
                    deck.append((i - r) % (n))
        deck = deque(set(deck))
    
    ans = set(deck)
    print(len(ans))
    
    print(*sorted(ans))
    


    



T = I()
for _ in range(T):
    solve()