class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            m = min(len(a), len(b))
            l = 0
            while l < m:
                if order.index(a[l]) > order.index(b[l]) and a[:l] == b[:l]:
                    print(a[l], b[l])
                    return False
                l += 1
            print(l,len(b) - 1,len(a) - l)
            if  len(a) - l > 0 and len(b) - l == 0 and a[:l] == b[:l]:
                return False
            
        return True
                


