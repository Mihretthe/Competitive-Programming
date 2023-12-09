n = int(input())
nums = list(map(int, input().split()))
nums.sort()
n = nums[:]
n.sort(key = lambda x : x % 2 == 0)
s = sum(nums)
if s % 2 == 0:
    print(s)
else:
    s -= n[0]
    print(s)
