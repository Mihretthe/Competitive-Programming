class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i <len(nums):
            z=nums.count(nums[i])
            if nums.count(nums[i])>2:
                for j in range(i+2,i+z):
                    nums[j]="_"
            i+=z
        t=[]
        for i in nums:
            if i!="_":
                t.append(i)
        j=0
        while j<len(t):
            nums[j]=t[j]
            j+=1
        return len(t)