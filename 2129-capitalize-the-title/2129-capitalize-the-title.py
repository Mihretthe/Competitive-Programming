class Solution:
    def capitalizeTitle(self, title: str) -> str:
        t=title.split(" ")
        for i in range(len(t)):
            t[i]=t[i].lower()
            if len(t[i])>2:
                s=[]
                for j in t[i]:
                    s.append(j)
                s[0]=s[0].upper()
                t[i]="".join(s)
        return " ".join(t)        
        
            