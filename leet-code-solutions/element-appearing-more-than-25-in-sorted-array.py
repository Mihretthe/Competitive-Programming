class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = int(len(arr) * 0.25)

        counter = Counter(arr)

        for i in counter:
            if counter[i] > n:
                return i
