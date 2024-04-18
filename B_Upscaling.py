
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
from collections import defaultdict
    

def solve():
    

    n = int(input())

    for i in range(2 * n):
        if (i // 2) % 2 == 0:
            flag = True
            line = []
            for i in range(n):
                if flag:
                    line.append("##")
                    flag = False
                else:
                    line.append("..")
                    flag = True
        else:
            flag = True
            line = []
            for i in range(n):
                if not flag:
                    line.append("##")
                    flag = True
                else:
                    line.append("..")
                    flag = False

        print("".join(line))
    # print()


    

    
    
    
    
T = I()
for _ in range(T):   
    solve()
    