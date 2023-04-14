class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        a=s.split(" ")
        a=reversed(a)
        b=[]
        for i in a:
            if i.isalnum():
                b.append(i)
            else:
                continue
        return " ".join(b)