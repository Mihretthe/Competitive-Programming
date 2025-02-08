from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

class Node:
    def __init__(self, val,):
        self.value = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.dummy = Node(-1)
        self.tail = self.dummy
                
    
    def delete(self, node):
        if node == self.tail:
            self.tail = node.prev
        if node.prev and node.next:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            node.next = None
            node.prev = None
            
        elif node.prev:
            node.prev.next = None
        elif node.next:
            node.next.prev = None
        
    def insert(self, after, node):
        if after == None:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:        
            nxt = after.next
            after.next = node
            node.prev = after
            if nxt:
                nxt.prev = node
                node.next = nxt
        if node.next == None:
            self.tail = node
       
        return node


from collections import defaultdict, deque

def solve():
    n = I()
    hashmap = defaultdict(deque)
    linked = LinkedList()

    for _ in range(n):
        a = input().split()
        if len(a) == 3:
            x, y = int(a[1]), int(a[2])
            if  hashmap[y]:                
                hashmap[x].append(linked.insert(hashmap[y][0], Node(x)))
            else:
                hashmap[x].append(linked.insert(None, Node(x)))
        else:
            x = int(a[1])
            
            if len(hashmap[x]) > 0:
                node = hashmap[x].popleft()
                linked.delete(node)
    answer = []
    head = linked.dummy.next

    while head:
        answer.append(head.value)
        head = head.next
    
    print(*answer)

 
T = 1
for _ in range(T):
    solve()