class Solution:
    def isValid(self, s: str) -> bool:
        a=list()
        c=bool()
        if len(s)%2!=0:
            return False
        for i in s:
            if i=="(" or i=="[" or i=="{":
                a.append(i)
            elif len(a)==0 and i=="]" or len(a)==0 and i==")" or len(a)==0 and i=="}":
                c=False
            elif len(a)>=1 and i=="]" or i==")" or i=="}":
                x=a.pop(-1)
                if i=="]" and x=="[" or i==")" and x=="(" or i=="}" and x=="{":
                    c=True
                else:
                    return False
        if len(a)>0:
            return False
        return c