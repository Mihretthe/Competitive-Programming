count = 0
for _ in range(int(input())):
    problems = list(map(int, input().split()))
    if problems.count(1) > 1:
        count += 1
print(count)
