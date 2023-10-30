class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        hashmap = defaultdict(list)
        for i in arr:
            s = bin(i)
            n = s.count("1")
            hashmap[n].append(i)
        key = list(hashmap.keys())
        key.sort()
        ans = []
        for i in key:
            ans += sorted(hashmap[i])
        return ans
        