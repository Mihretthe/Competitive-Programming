class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        indexes = defaultdict(list)
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] in indexes:
                for index in indexes[nums[i]]:
                    if (index * i) % k == 0:
                        count += 1
            indexes[nums[i]].append(i)

        return count
            

        
            

