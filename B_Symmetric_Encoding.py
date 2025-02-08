from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    decoded_s = S()

    alphabet = list(set(decoded_s))
    alphabet.sort()

    left = 0
    right = len(alphabet) - 1

    dictionary = {}

    while left <= right:
        dictionary[alphabet[left]] = alphabet[right]
        dictionary[alphabet[right]] = alphabet[left]
        left += 1
        right -= 1
    
    encoded = []
    
    for i in decoded_s:
        encoded.append(dictionary[i])
    
    print("".join(encoded))

 
 
 
 
T = I()
for _ in range(T):
    solve()