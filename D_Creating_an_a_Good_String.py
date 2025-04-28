from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def change(char):
    return chr(ord(char) + 1)

def solve():
    n = I()
    s = S()
    
    def recursion(s, character):
        if len(s) == 1:
            if s == character:
                return 0
            return 1

        mid = len(s) // 2
        
        left = mid - s[:mid].count(character) + recursion(s[mid:], change(character))
        right = mid - s[mid:].count(character) + recursion(s[:mid], change(character))
        
        return min(left, right)

    print(recursion(s, 'a'))
 
 
 
 
T = I()
for _ in range(T):
    solve()
    