from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

# If I have the indices of the previus smaller and the next smaller then I can know the window size

next_smaller = [10] * n
previous_smaller = [-1] * n

stack = []
for i in range(n):
    while stack and nums[stack[-1]] > nums[i]:
        next_smaller[stack.pop()] = i

    stack.append(i)

stack = []
for i in range(n):
    while stack and nums[stack[-1]] >= nums[i]:
        stack.pop()

    if stack:
        previous_smaller[i] = stack[-1]

    stack.append(i)

hashmap = defaultdict(int)

for i in range(n):
    if previous_smaller[i] == -1:
        hashmap[next_smaller[i]] = max(nums[i], hashmap[next_smaller[i]])
    else:
        val = next_smaller[i] - previous_smaller[i] - 1
        hashmap[val] = max(nums[i], hashmap[val])

answer = [-1] * n

for key, value in hashmap.items():
    answer[key - 1] = value

for i in range(n - 2, -1, -1):
    answer[i] = max(answer[i], answer[i + 1])

print(*answer)
