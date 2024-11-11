class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def is_prime(num):
            for i in range(2, isqrt(num) + 1):
                if num % i == 0:
                    return False
            
            return True

        array = []

        for i in range(2, 10000):
            if is_prime(i):
                array.append(i)
        
        
        length = len(nums)

        for i in range(length - 2, -1, -1):
            if nums[i + 1] <= nums[i]:
                num = nums[i] - nums[i + 1]
                index = bisect_left(array, num + 1)
                nums[i] -= array[index]

        # print(nums)
        return sorted(nums) == nums and nums[0] > 0