class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for i in range(len(order)):
            hashmap[order[i]] = i
        



        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            m = min(len(a), len(b))
            l = 0

            while l < m:
                if hashmap[a[l]] > hashmap[b[l]] and a[:l] == b[:l]:
                    return False
                l += 1
            if  len(a) - l > 0 and len(b) - l == 0 and a[:l] == b[:l]:
                return False
            
        return True
                


