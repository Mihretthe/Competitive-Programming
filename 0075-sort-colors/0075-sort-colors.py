# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if(nums[i]<nums[j]):
        #             nums[i],nums[j]=nums[j],nums[i]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        for i in nums:
            counter[i] += 1
        new_arr = []
        
        for i in range(3):
            new_arr += ([i] * counter[i]) 
        for i in range(len(nums)):
            nums[i] = new_arr[i]
                    
        
        
        
