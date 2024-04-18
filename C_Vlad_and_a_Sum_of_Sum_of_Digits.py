def sumd(num):
    ans = 0
    while num > 0:
        ans += num % 10
        num //= 10
    return ans
answer = []

for i in range(1, 200001):
    if not answer:
        answer.append(i)
    else:
        answer.append(answer[-1] + sumd(i))


for _ in range(int(input())):
    n = int(input())
    print(answer[n - 1])
    
    