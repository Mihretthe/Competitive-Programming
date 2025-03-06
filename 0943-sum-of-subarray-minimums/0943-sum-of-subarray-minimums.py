class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1000000007
        length = len(arr)
        next_smaller = [length] * length
        previous_smaller = [-1] * length

        stack = []
        for i in range(length):
            
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                next_smaller[index] = i
            stack.append(i)
            
        
        stack = []
        for i in range(length - 1, -1, -1):
            
            while stack and arr[stack[-1]] >= arr[i]:
                index = stack.pop()
                previous_smaller[index] = i
            stack.append(i)

        answer = 0
        for i in range(length):
            
            left = i - previous_smaller[i]
            right = next_smaller[i] - i

            answer += (left* right * arr[i])


        return answer % MOD

            