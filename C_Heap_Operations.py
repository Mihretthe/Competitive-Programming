from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from heapq import heapify, heappop, heappush 

def solve():
    length = I()
    heap = []
    answer = []
    for _ in range(length):
        command = SL()
        if len(command) == 2:
            command, num = command
            num = int(num)
            if command == "insert":
                heappush(heap, num)
                answer.append([command, num])
            else:
                if not heap:
                    heappush(heap, num)
                    answer.append(["insert", num])
                    answer.append([command, num])
                else:
                    # answer.append(heap)
                    if  heap[0] == num:
                        answer.append([command, heap[0]])
                    elif  heap[0] > num:
                        answer.append(["insert", num])
                        heappush(heap, num)
                        answer.append([command, num])
                    else:
                        heappush(heap, num)
                        while heap and heap[0] < num:
                            answer.append('removeMin')
                            heappop(heap)
                        answer.append(["insert", num])
                        answer.append([command, num])                        
        else:
            if heap:
                heappop(heap)
            else:
                answer.append(['insert', 0])
                # heappush(heap, 0)
                # heappop(heap)
            answer.append(command[0])

    print(len(answer))
    for command in answer:
        if len(command) == 2:print(*command)
        else: print(command)

 
 
 
 
T = 1
for _ in range(T):
    solve()