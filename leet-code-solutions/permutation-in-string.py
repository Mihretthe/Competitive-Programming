class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        min_length = len(s1)
        counter = Counter(s1)

        for i in range(len(s2)):
            if Counter(s2[i: i + min_length]) == counter:
                return True
        return False