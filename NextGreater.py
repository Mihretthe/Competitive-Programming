def findNextGreater(nums):
    #using monotonic non increasing stack

    length = len(nums)
    stack = []
    nextGreater = [-1] * length

    for i in range(length):
        
        while stack and nums[stack[-1]] < nums[i]:
            nextGreater[stack.pop()] = nums[i]

        stack.append(i)

    return nextGreater

print(findNextGreater([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))