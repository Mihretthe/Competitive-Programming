from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import deque

def solve():
    n = I()
    nums = IL()

    def inbound(index):
        return index >= 0 and index < n
    answer = []

    for i in range(n):
        node = nums[i]
        deck = deque([(node, node % 2, 1)])
        
        visited = set([i])
        while deck:
            ans = float('inf')
            print(deck)
            node, parity, level = deck.popleft()
            flag = False
            left = i - node
            right = i  + node
            if left not in visited:
                
                if inbound(left) and nums[left] % 2 != parity:
                    ans = min(ans, level )
                    flag = True
                elif inbound(left):
                    visited.add(left)
                    deck.append((nums[left], nums[left] % 2, level + 1))
            if right not in visited:
                
                if inbound(right) and nums[right] % 2 != parity:
                    ans = min(ans, level)
                    answer.append(ans)
                    break
                elif inbound(right):

                    visited.add(right)
                    deck.append((nums[right], nums[right] % 2, level + 1))
            if flag:
                answer.append(ans )
                break
        else:
            answer.append(-1)
        
        
    print(*answer)
                
 
 
 
 
T = 1
for _ in range(T):
    solve()