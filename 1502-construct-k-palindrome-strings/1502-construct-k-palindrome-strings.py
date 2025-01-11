class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counter = Counter(s)

        if len(s) < k:
            return False

        count = 0
        
        for i in counter:
            if counter[i] % 2:
                count += 1

        return count <= k