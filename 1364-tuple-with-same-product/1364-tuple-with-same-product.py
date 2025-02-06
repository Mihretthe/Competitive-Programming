class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = Counter()
        length = len(nums)

        for i in range(length):
            for j in range(i + 1, length):
                counter[nums[i] * nums[j]] += 1
    
        answer = 0

        for key, value in counter.items():
            answer += (value) * (value - 1)

        return 4 * answer