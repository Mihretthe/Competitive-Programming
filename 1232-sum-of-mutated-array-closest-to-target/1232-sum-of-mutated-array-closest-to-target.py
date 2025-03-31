class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        length = len(arr)

        def check(value):
            total = 0

            for i in range(length):
                if arr[i] > value:
                    total += value
                else:
                    total += arr[i]
                
            return total
        
        left = 0
        right = max(arr)

        while left <= right:
            mid = (left + right) // 2
            value = check(mid)

            if value >= target:
                right = mid - 1
            else:
                left = mid + 1

        val1 = abs(check(left) - target)
        val2 = abs(check(right) - target)

        if val1 >= val2:
            return right
        
        return left


            

