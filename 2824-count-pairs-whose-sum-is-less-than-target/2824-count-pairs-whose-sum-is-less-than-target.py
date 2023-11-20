class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        a = list(enumerate(nums))
        a.sort(key = lambda x : x[1])
        count = 0
        for i in range(len(nums)):
            val = a[i][1]
            for j in range(i + 1,len(nums)):
                if val + a[j][1] < target:
                    count += 1
        return count