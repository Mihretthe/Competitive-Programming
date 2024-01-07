class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        k = len(p)
        counter_p = Counter(p)
        

        for i in range(len(s) - k + 1):
            if Counter(s[i:i + k]) == counter_p:
                ans.append(i)

        return ans
