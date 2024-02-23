from collections import Counter, defaultdict

length = int(input())
nums = list(map(int, input().split()))

counter = Counter(nums)
multiple = defaultdict(list)

if length > len(counter):
    for i in range(length):
        if counter[nums[i]] > 1:
            multiple[nums[i]].append(i)  
            

    l = float('inf')
    r = 0

    for i in multiple:
        l = min(l, multiple[i][1])
        r = max(r, multiple[i][-1])

    print(r - l + 1)
else:
    print(0)