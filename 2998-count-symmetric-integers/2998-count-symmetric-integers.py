class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def helper(num):

            num = str(num)
            if len(num) % 2:
                return 0
            
            mid = len(num) // 2
            if sum([int(i) for i in num[:mid]]) == sum([int(i) for i in num[mid:]]):
                return 1
            return 0

        answer = 0
        for num in range(low, high + 1):
            answer += helper(num)
        
        return answer


            