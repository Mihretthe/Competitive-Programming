from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    r, b = II()
    
    # if I choose red
    order = []
    turn = True
    countr = r
    countb = b
    
    for _ in range(r + b):
        if turn:
            if order:
                last = order[-1]
                if last == "r":
                    if countr > 0:
                        order.append("r")
                        countr -= 1
                    else:
                        order.append("b")
                        countb -= 1
                else:
                    if countb > 0:
                        order.append("b")
                        countb -= 1
                    else:
                        order.append("r")
                        countr -= 1
            else:
                if countr > 0:
                    order.append("r")
                    countr -= 1
                else:
                    order.append("b")
                    countb -= 1
            turn  = False
        else:
            last = order[-1]
            if last == "r":
                if countb > 0:
                    order.append("b")
                    countb -= 1
                else:
                    order.append("r")
                    countr -= 1
            else:
                if countr > 0:
                    order.append("r")
                    countr -= 1
                else:
                    order.append("b")
                    countb -= 1
                            
            turn  = True
    first = (order[:])
    
    order = []
    turn = True
    countr = r
    countb = b
    
    for _ in range(r + b):
        if turn:
            if order:
                last = order[-1]
                if last == "r":
                    if countr > 0:
                        order.append("r")
                        countr -= 1
                    else:
                        order.append("b")
                        countb -= 1
                else:
                    if countb > 0:
                        order.append("b")
                        countb -= 1
                    else:
                        order.append("r")
                        countr -= 1
            else:
                if countb > 0:
                    order.append("b")
                    countb -= 1
                    
                else:
                    
                    order.append("r")
                    countr -= 1
                    
            turn  = False
        else:
            last = order[-1]
            if last == "r":
                if countb > 0:
                    order.append("b")
                    countb -= 1
                else:
                    order.append("r")
                    countr -= 1
            else:
                if countr > 0:
                    order.append("r")
                    countr -= 1
                else:
                    order.append("b")
                    countb -= 1
                            
            turn  = True
    
    
    p = 0
    v = 0
    
    for i in range(len(first) - 1):
        if first[i] == first[i + 1]:
            p += 1
        else:
            v += 1
    
    p2, v2 = 0, 0
    
    for i in range(len(order) - 1):
        if order[i] == order[i + 1]:
            p2 += 1
        else:
            v2 += 1
    
    
    # print(p, v)
    # print(p2, v2)
    
    if p2 > p:
        print(p2, v2)
    else:
        print(p, v)
        
 
 
 
T = 1
for _ in range(T):
    solve()