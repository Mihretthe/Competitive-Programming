class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        i=0
        c=[]
        a=[]
        nums.sort()
        while i<len(nums):
            c.append(list((nums.count(nums[i]),nums[i])))
            i+=nums.count(nums[i])
        c.sort(reverse=True)
        for i in range(k):
            a.append(c[i][1])
        return a