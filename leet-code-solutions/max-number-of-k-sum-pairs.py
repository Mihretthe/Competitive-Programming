class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        count = 0
        
        for i in counter:
            while k - i in counter and counter[i] > 0 and counter[k - i] > 0:
                if i == (k - i) and counter[i] == 1:
                    break
                counter[i] -= 1
                counter[k - i] -= 1
                count += 1

        return count