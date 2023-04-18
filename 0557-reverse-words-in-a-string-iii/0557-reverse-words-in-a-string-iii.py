class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split(" ")
        for i in range(len(a)):
            a[i]=a[i][::-1]
        return " ".join(a)    
        