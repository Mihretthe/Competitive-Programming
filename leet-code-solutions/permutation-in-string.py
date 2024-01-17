class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        length_2 = len(s2)
        counter_1 = Counter(s1)
        counter = Counter(s2[:k])
        left = 0
        if counter_1 == counter:
            return True

        for right in range(k,length_2):
            counter[s2[left]] -= 1
            if counter[s2[left]] == 0:
                del counter[s2[left]]
            counter[s2[right]] += 1
            if counter == counter_1:
                return True
            left += 1

        return False


