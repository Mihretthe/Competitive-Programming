class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        a=words[0]
        n=[]
        for i in a:
            for j in words[1:]:
                c=False
                if i in j:
                    c=True
                    words[words.index(j)]=j[:j.index(i)]+"_"+j[j.index(i)+1:]
                else:
                    break
            if c==True:
                n.append(i)
        return n