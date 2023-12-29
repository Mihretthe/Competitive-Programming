class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        
        s.sort(key = lambda x : x[-1])
        s = list(map(lambda x : x[:-1], s))

        return " ".join(s)