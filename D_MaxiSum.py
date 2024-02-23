n, q = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0] * n

for _ in range(q):
    l, r = map(int, input().split())
    prefix[l - 1] += 1
    if r < n:
        prefix[r] -= 1

for i in range(1, n):
    prefix[i] += prefix[i - 1]

nums.sort(reverse = True)
prefix.sort(reverse = True)

answer = 0

for num, freq in zip(nums, prefix):
    answer += (num * freq)

print(answer)

    