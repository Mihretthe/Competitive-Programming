class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, temp = [], temperatures
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                j = stack.pop()
                temp[j] = i - j
            stack.append(i)
        for _ in range(len(stack)):
            temp[stack.pop()] = 0
        return temp