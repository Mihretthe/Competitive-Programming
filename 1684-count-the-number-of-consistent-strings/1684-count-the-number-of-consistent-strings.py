class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        words=[set(i) for i in words]
        words=["".join(list(i)) for i in words]
        c=0
        for i in words:
            a=True
            for j in i:
                if j not in allowed:
                    a=False
                    break
            if a:
                c+=1
        return c