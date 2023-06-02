class Solution:
    def reorderSpaces(self, text: str) -> str:
        a=text.count(" ")
        text=text.strip()
        text=text.split()
        if len(text)>1:
            n=a//(len(text)-1)
            s=" "*n
            return s.join(text)+" "*(a%(len(text)-1))
        return "".join(text)+" "*a