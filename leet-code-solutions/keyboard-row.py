class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a="qwertyuiopQWERTYUIOP"
        d=1
        b="asdfghjklASDFGHJKL"
        e=2
        c="zxcvbnmZXCVBNM"
        f=3
        h=[]
        for i in words:
            x=set()
            for j in i:
                if j in a:
                    x.add(d)
                elif j in b:
                    x.add(e)
                elif j in c:
                    x.add(f)
            if len(x)==1:
                h.append(i)
        return h