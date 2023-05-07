class Solution:
    def minTimeToType(self, word: str) -> int:
        n=len(word)
        s="abcdefghijklmnopqrstuvwxyz"
        pre="a"
        for i in word:
            v=(s.index(i)-s.index(pre))%26
            n+=min(v,26-v)
            pre=i
        return n