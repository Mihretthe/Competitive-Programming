class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        arr = []

        for i in range(n):
            arr.append(x[i])
            arr.append(y[i])

        return arr