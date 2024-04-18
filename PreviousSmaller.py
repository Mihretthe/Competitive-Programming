def findPreviousSmaller(nums):
    # using monotonic strictly increasing stack

    length = len(nums)
    stack = []
    previousSmaller = [-1] * length

    for i in range(length):

        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()

        if stack:
            previousSmaller[i] = nums[stack[-1]]

        stack.append(i)

    return previousSmaller

print(findPreviousSmaller([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))