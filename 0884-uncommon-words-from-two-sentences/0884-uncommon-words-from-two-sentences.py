class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split(" ")
        s2=s2.split(" ")
        a=[x for x in s1 if s1.count(x)==1 and x not in s2]        
        b=[x for x in s2 if s2.count(x)==1 and x not in s1]   
        return a+b