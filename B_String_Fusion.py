from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

class TrieNode:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.count = 0

def solve():
    
    root = TrieNode()
    array = []
    n = I()
    
    lenn = 0

    for _ in range(n):
        word = S()
        array.append(word)
        lenn += len(word)


        pointer = root
        for letter in word:
            index = ord(letter) - 97
            if not pointer.children[index]:
                pointer.children[index] = TrieNode()
            
            pointer = pointer.children[index]
            pointer.count += 1
        
        pointer.is_end = True

    
    tot = 0
    for i in array:
        tot += len(i) * n + lenn
    
    
    for word in array:
        word = word[::-1]
        count = 0

        pointer = root
        
        for letter in word:
            index = ord(letter) - 97
            if not pointer.children[index]:
                break
            count += pointer.children[index].count
            pointer = pointer.children[index]
            
        tot -= 2 * count
    
    print(tot)



 
T = 1
for _ in range(T):
    solve()