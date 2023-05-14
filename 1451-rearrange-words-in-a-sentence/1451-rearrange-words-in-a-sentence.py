class Solution:
    def funLen(self, a):
        return len(a)
    def arrangeWords(self, text: str) -> str:
        text=text.split()
        text=[x.lower() for x in text]
        text.sort(key=self.funLen)
        text[0]=text[0][0].upper()+text[0][1:]
        return " ".join(text)
        