class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        bit = [0] * 32
        mini = inf

        def build(array):
            num = 0
            for i in range(32):
                if array[i] > 0:
                    num |= 1 << i
            
            return num


        left = 0
        length = len(nums)

        for right in range(length):

            for i in range(32):
                bit[i] += int(bool(nums[right] & 1 << i))
            
            num = build(bit)

            while left <= right and num >= k:
                mini = min(mini, right - left + 1)
                for i in range(32):
                    bit[i] -= int(bool(nums[left] & 1 << i))
                num = build(bit)
                left += 1
            
        if mini == inf:
            return -1
        
        return mini
            

            


            