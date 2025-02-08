from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    s = S()

    if n - 2 <= 0:
        print(int(s))
        return 
    
    array = list(map(int, s))

    def create(i):
        return array[:i] + [array[i] * 10 + array[i + 1]] + array[i + 2:]
    

    def dp(index):
        if index not in memo:
            if index == len(new_array) - 1:
                return new_array[index]

            plus = new_array[index] + dp(index + 1)
            mul = new_array[index] * dp(index + 1)

            memo[index] = min(plus, mul)

        return memo[index]
    
    mini = float('inf')

    for i in range(n - 1):
        memo = {}
        new_array = create(i)
        mini = min(mini, dp(0))

    print(mini)

    


T = I()
for _ in range(T):
    solve()
    