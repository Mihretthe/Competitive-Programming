class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        counter_p = defaultdict(int)
        counter_s = defaultdict(int)
        k = len(p)
        n = len(s)

        if k > n:
            return []

        for i in range(k):
            counter_p[p[i]] += 1
            counter_s[s[i]] += 1

        if counter_s == counter_p:
            indices.append(0)
        for start in range(1, n - k + 1):
            counter_s[s[start - 1]] -= 1
            counter_s[s[start + k - 1]] += 1
            if counter_s[s[start - 1]] == 0:
                del counter_s[s[start - 1]]
            if counter_s == counter_p:
                indices.append(start)

        return indices
            