from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

"""
condition = smallest if the count of the smallest is available
end of completion if one of them is ended
"""

def solve():
    n, m, k = II()
    a = sorted(S())[::-1]
    b = sorted(S())[::-1]
    answer = []
    count_a = 0
    count_b = 0

    while a and b:
        if a[-1] <= b[-1]:
            if count_a < k:
                answer.append(a.pop())
                count_a += 1
                count_b = 0
            else:
                answer.append(b.pop())
                count_b += 1
                count_a = 0
        else:
            if count_b < k:
                answer.append(b.pop())
                count_b += 1
                count_a = 0
            else:
                answer.append(a.pop())
                count_a += 1
                count_b = 0

    print("".join(answer))


    


 
 
 
 
T = I()
for _ in range(T):
    solve()