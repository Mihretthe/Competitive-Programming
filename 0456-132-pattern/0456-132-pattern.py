class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        
#         for i in range(len(nums)):
#             a = [nums[i]]
#             n = len(nums) - 1
#             while n > 0:
#                 if nums[n] > a[0]:
#                     a .append(nums[n])
#                     break
#                 n -= 1
#             if len(a) == 2 and max(nums[:n]) > max(a):
#                 return True
#         return False
        a = []
        m = nums[0]
        for i in nums:
            while a and i >= a[-1][0]:
                a.pop()

            if a and i > a[-1][1]:
                return True

            a.append([i,m])
            m=min(m,i )
        return False      
        
        