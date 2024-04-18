from collections import deque

n, q = map(int, input().split())
a = deque(map(int, input().split()))
maxi = max(a)

answers = []

for i in range(n):
    if a[0] == maxi:        
        break
    A = a.popleft()
    B = a.popleft()
    answers.append([A,B])
    if A > B:
        a.appendleft(A)
        a.append(B)
    else:
        a.appendleft(B)
        a.append(A)
    if a[0] == maxi:
        a.popleft()      
        break
    
# print(a)


for _ in range(q):
    m = int(input()) 
    if m <= len(answers):
        print(*answers[m - 1])
    else:
        print(maxi, a[((m - 1) % (n - 1))])

