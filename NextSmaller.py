def findNextSmaller(nums):
    #using non decreasing monotonic stack

    length = len(nums)
    stack = []
    nextSmaller = [-1] * length

    for i in range(length):

        while stack and nums[stack[-1]] > nums[i]:
            nextSmaller[stack.pop()] = nums[i]

        stack.append(i)

    return nextSmaller

print(findNextSmaller([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))
