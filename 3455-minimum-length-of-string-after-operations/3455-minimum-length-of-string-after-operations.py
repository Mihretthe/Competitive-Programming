class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)

        count = 0

        for key, value in counter.items():
            if value < 3:
                count += value
            else:
                if value % 2:
                    count += 1
                else:
                    count += 2

        
        return count